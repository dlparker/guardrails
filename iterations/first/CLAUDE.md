# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a tool for importing credit card transaction CSV files (as downloaded from banks) into GnuCash files as properly balanced transactions. The project is partially complete with a working core workflow, and is currently in the UI development/experimentation phase.

## Core Architecture

### State-Machine Workflow (MainFlow)

The application follows a strict state machine pattern defined in `src/ctrack/flow.py`. The `MainFlow` class orchestrates the entire import process through a series of required steps:

1. **SET_GNUCASH** - Identify the target GnuCash file
2. **LOAD_XACTION_FILE** - Load a credit card CSV file
3. **ADD_COLUMN_MAP** - Map CSV columns to expected fields (Date, Payee, Amount, date format)
4. **ADD_MATCHER_RULE** - Create regex rules to match transactions to GnuCash accounts
5. **ADD_ACCOUNT** - Define missing accounts in local database
6. **DO_ACCOUNT_SYNC** - Sync local accounts to GnuCash file
7. **SAVE_XACTIONS** - Write balanced transactions to GnuCash

The workflow is enforced via `get_next_step()` and `get_data_needs()` methods. Understanding this flow is critical - see `tests/test_flow.py` for the complete workflow demonstration.

### Data Layer (DataService)

`src/ctrack/data_service.py` provides all database operations using SQLAlchemy with SQLite. Key models:

- **MetaData** - Stores GnuCash file path
- **ColumnMap** - CSV column mappings with date format
- **MatcherRule** - Regex patterns for transaction categorization (has `compiled` property for matching)
- **Account** - Local account definitions with sync status (`in_gnucash` flag)
- **CCTransactionFile** - Imported CSV file records with mapping/matching status
- **CCTransactionsRaw** - Raw CSV rows
- **CCTransaction** - Processed transactions linked to MatcherRule

The DataService uses a local SQLite database (in the working directory) to track state. GnuCash files are accessed via the `piecash` library.

### UI Experiments (In Progress)

Three UI approaches are being explored:

1. **NiceGui** - `src/ctrack/ng/` and `scripts/ng_main.py` (experimental, not production-ready)
2. **Textual** - `src/ctrack/textual/` and `scripts/tx_main.py` (stub only)
3. **Flet** - Not yet started

All UIs should wrap the MainFlow state machine, not bypass it.

## Development Commands

### Setup Working Environment

```bash
uv run scripts/prep_work.py         # Copy demo files to demo_work/
uv run scripts/prep_work.py -r      # Reset: delete existing files first
```

This copies files from `demo_data/` to `demo_work/` for testing. Includes a test GnuCash file and sample CSV files.

### Testing

```bash
uv run pytest                        # Run all tests with coverage
uv run pytest tests/test_flow.py     # Run single test file
uv run pytest -k test_full_flow      # Run specific test
uv run pytest -v                     # Verbose output
```

Coverage reports are generated in `htmlcov/` directory. The test suite uses pytest with coverage configured in `pytest.ini` (current: 27% coverage).

### Running UI Experiments

```bash
uv run scripts/ng_main.py            # NiceGui experimental UI
uv run scripts/tx_main.py            # Textual stub
```

## Key Implementation Details

### Transaction Matching Process

1. CSV loaded via `DataService.load_transactions()`
2. Columns mapped using existing ColumnMap or user creates new one
3. Each raw transaction checked against MatcherRule patterns (case-insensitive option available)
4. Matched transactions linked to MatcherRule, which specifies target account
5. Accounts validated against GnuCash file before save

### Account Sync Pattern

Accounts exist in three states:
- Not in local DB → Add to DB via `add_account()`
- In DB but `in_gnucash=False` → Sync to GnuCash via `save_account()`
- In DB and `in_gnucash=True` → Ready to use

The `save_to_gnucash()` method on CCTransactionFile requires credit card liability account and payments account names.

### SQLite Decimal Handling

Custom `SqliteDecimal` TypeDecorator in `data_service.py` handles monetary values by storing as integers (scaled by 100) to avoid floating-point issues.

## Project Structure

```
src/ctrack/
├── flow.py          # MainFlow state machine
├── data_service.py  # DataService + SQLAlchemy models
├── ng/              # NiceGui UI experiment
└── textual/         # Textual UI stub

scripts/
├── prep_work.py     # Demo environment setup
├── ng_main.py       # NiceGui entry point
└── tx_main.py       # Textual entry point

tests/
├── test_flow.py     # Complete workflow test
├── test_dataservice.py
└── prep_data/       # Test fixtures

demo_data/           # Source files for UI development
demo_work/           # Working directory for UI testing (gitignored)
```

## Important Notes

- The project uses `uv` for dependency management
- Python 3.12+ required
- All CSV imports must match a ColumnMap for date/payee/amount fields
- Matcher rules use Python regex with optional case-insensitive flag
- GnuCash files are opened via piecash library (read/write support)
- The workflow enforces data validation before allowing saves to GnuCash
- Check `tests/test_flow.py` for canonical usage patterns - this test demonstrates the complete happy path
