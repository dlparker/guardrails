
This project is a partially complete tool for importing credit card statements as downloaded
from banks into a GnuCash file as properly balanced transactions.

The currently working parts of the tool can be deduced from examining the code in 
tests/test_flow.py and the elements that it uses from the source tree. 

The current stage of the project involves experimenting with different approaches
to building a UI on top of the working functionality. The possible choices are:

1. Nicegui - there is some experimental code for this already, but it does not exhibit any sort of approved UX, it is just an experiment for the project lead human to study. The code is in src/ctrack/ng and scripts/ng_main.py
2. Textual - there is stub that ensures that the project is configure to run a textual app. The code is in src/ctrack/textual and scripts/tx_main.py
3. Flet - Nothing yet


There are some files prepared to support UI development, and there is a tool for preparing those files in scripts/prep_work.py.

You can run it with 'uv run scripts/prep_work.py' with the optional -r for resting by deleting all existing files in demo_work.
