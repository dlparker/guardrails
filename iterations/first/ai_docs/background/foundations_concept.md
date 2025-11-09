## Using the Framework in Guidance

## Discussion: Balance

One factor in the skill of producing usable code at a
higher rate than the average developer is in finding a good balance
between getting something done fast enough to move the project forward
as soon as possible, and building something so good that there is
never any need to re-write it. Although some people are tempermentally
constrained to one end of the spectrum or the other, most developers
oscillate back and forth for a variety of reasons related to
motivations, emotional state and pressures of the job. Having a structured
way to think about the balancing act can help. 

It is a dymanic process where choices need to be made at a pretty
granular level, sometimes all they way down to the level of a task
that might only take a few hours to complete. When using an iterative
development process where ship-able code emerges at the end of some
number of loops (you are doing it that way, right?), the proper
balance for a given peice of code might and often does change over
each iteration of the build-break-fix cycle.

It is possible to use a conceptual model to help **think and
communicate clearly** about what constitutes the **“right” balance**
for a particular part of a particular project at a particular time —
and the variables along each of those dimensions that help identify
what is “right”.

For that purpose, this conceptual framework that analogizes 
based on the way westerners established their presence in North America.
The phases are exploring, pioneering, and settling, fortifying, and re-founding.

Exploring is finding out what is there, and either moving on or
shifting to pioneering. In analogy land, when an explore enters a new
valley, he might put up a tent or build a lean-to situated so that he
can make day trips to different parts of the valley and return to the
camp at night. A software developer might write a little code to setup
for testing some idea such as using an API or finding out what is in a
file, but the effort is kept to the minimum to because too little is
known to justify building something re-usable.

Pioneering is establishing just enough infrastructure to support
immediate access to the discovered resources. In anology land, I
imagine the intrepid single family carving out a small farmstead in an
otherwise unpopulated valley. In software world this means writing
code that delivers enough value to allow you to use it to support
efforts in other areas of the project, but with minimal investment
in the code for structure, configuration, performance, reliability,
error handling, API design, etc. Pioneering may be the limit of
development in a particular location, or the development may progress
to settling.

Settling is developing the infrastructure needed for accessing the
location's value for the long term, but without premature investments
in future infrastructure. In anology land, imagine a group of families working
together to establish farms and some basic shared infrastructure such
as a mill or maybe fortified habitation and common food storage. In 
the software world this means adding enough structure to support
some features such as configuration, state discovery, better API
for cleaner integration with the rest of the system, etc. 

Fortifying is enhancing the infrastructure so that the resouces are
accessed more efficiently and with less reliance on outside help.  In
anology land, the settlement becomes a fort or town and becomes more
sustainable and self-sustaning. New shared facilties are constructed,
may things such as a blacksmith's shop, maybe a dock on the river or
bay for trading vessels, etc. For software this often means a refactoring to
improve common features of production code, such as clearer and more
comprehensive APIs and configuration opertions, integration with
external logging and error handling components, theory of operation
documentation, support for automated doc tools for internal
documention e.g. docstring formatting and type annotations for
methods/functions in python. This type of code could be shipped as
product, but is thought likely to need significant future enhancement
or restructuring if likely future requirements become active.

ReFounding is enhancing or replacing major parts of the infrastructure
to support a much expand range and qualtity of usage. In anology land, 
the town becomes a small city with significant physical infrastructure such as roads,
maybe railroads, large numbers of merchants and services, industrial
businesses, etc, and probably has to abandon or demolish and replace
original infrastructure.

I want to use it to describe the intentional stance that a
software developer should use when building code. So at the beginning,
when both the high level specifics of the problem to be solved and the
possible solution approaches are highly unclear, the developer should
be "exploring", that is writing code that illuminates where and how
the developer's thoughts about the problem and solution are wrong or
right. Once there is enough clarity, the developer should move on to
"pioneering".

## A story
A recent example of "exploring" for me was finding out some
basics for the idea of building a tool to assist in analyzing
downloaded credit card data so that I don't have to do it manually.
The desired analysis functions are categorizing and producing 
totals and trends for both individual item classes, e.g. Amazon 
Prime subscription as a item in the category online services. 
I wrote some simple code to build spreadsheets from the files. 
When I started thinking about how to create, organize and persist
the items and categories it occurred to me that I was re-tracing 
a well worn solution space, so I wondered if I could use somekind
of bookkeeping software to help. I experiemented with a coupld of 
ideas and ended up deciding that GnuCash was a possible solution,
especially because there is a nice python library for GnuCash files,
piecash.

I wrote some basic piecash code to export expense account data and 
use that to modify the import files to contain the account name in
the full gnucash path style, e.g. "Expenses:online_services:AmazonPrime".
I also wrote some basic pattern matching code to find clues in the 
credit card transactions and use those to map the transaction to 
an account. I tested the results by manually running the GnuCash
import processs. It tooks several iterations to understand all the 
requirements, such as how GnuCash handles the individual transactions
as balanced transactions.

At this point I had a pretty good idea of what steps to take to build
something that would at least partially automated this.

So the project moved into the "pioneering" phase, where began building 
components to 

1. read csv files for exported GnuCash accounts
2. hand built regular expression based "matchers" - matching rules to assign transactions to GnuCash accounts
3. read csv file and import contents as new GnuCash accounts
4. create modified transaction files that were suitable for import

Once I had some simple test code working on a trivial sample setup with only a couple
of accounts, a couple of matchers and a couple of transaction lines, I began
to build some tools to manage the workflow, using invocations of libreoffice calc
to allow me to edit and add data as implied about, i.e. define matchers, define new accounts.

The result of this phase seemed to indicate that this method of creating
the mapping data (matchers and accounts) might be good enough for the actual 
usable toolset, so the project moved into the "settlement" phase.

Operations in this phase 

1. Removed hard coding
2. Established some basic structure such as classes of functionality
3. Defining some dataclass classes for internal APIs
4. Building basic integration tests using pytest
5. Building a catalog of coordinated sets of csv files for start and end of workflow phases for various scenarios, incorporated them in tests.
6. Establishing some intenal verification of state.


The result of this phase was a complete flow that

1. exported GnuCash accounts to a csv
2. imported the csv
3. imported the set of matchers from a csv
4. created a csv of account paths named in the matchers that were missing from gnucash, started clac to request that user check and add a description value for each
5. used the resulting edited csv to add the accounts to gnucash
6. loaded a transaction csv file
7. tested each line in the transaction file against the matchers starting a calc instance to ask for new matcher definitions for missing lines.
8. checked the transaction file for matching and repeated step 7 if needed.
9. rechecked the matcher to account map and repeated steps 4 and 5 if necessary
10. create a new transaction file modified as needed for import

I wrote pytest integration tests to cover this worflow with various
condtions to excersize the decision loops, and used hand code result
files instead of running the calc process for user interaction. I got high 
enough code coverage to be confident that the process work.

As a result of this I found these deficiencies with the solution:

1. there was no way to validate user input in calc process, making it difficult to build matchers using regular expressions
2. the GnuCash import process is a bit tedious and it is easy to get a partial import when something doesn't match on one or more transactions, and this is hard to unwind and retry.

So, I moved into the "exploring" phase again to see if I now understood enough about GnuCash and piecash to do the import
programatically. I wrote some code to try this out, and found that it was straight forward. 

I new from previous experience that I could build an appriopriate UI using nicegui with an acceptable level effort and 
therefore address the lack of validation and other more minor usage annoyances.

So I moved back in the "settling" phase and wrote a nicegui single page app that:

1. Provided ways to identify the input files, e.g. test.gnucash, matchers.csv, transaction.csv.
2. Used the existing code to load the accounts, matchers, transactions.
3. Provided operations to request user to add matchers for unmatched transactions and acccounts for unsatisified matcher to account references.
3. Provided an "all good" check and offer of an action to import transactions into gnucash.

One result of this phase was the realization that the implementation was being negatively impacted by 
the effect of holding on to the original CSV file based approach that had made sense when libreoffice calc
was the UI. Another result was to realize that the UI app was holding too much "business logic" with 
the usual result of the presentation and buisness logic corrupting each other. So a new layer for 
providing the business logic as needed.

So a new "settling" phase began but with enough difference in approach that it was analogous to starting 
a totally new settlement. This consisted of:

1. Replacing the persistence model with one based on SqlAlchemy and Sqlite.
2. Building new functionality to do direct credit card transaction insert into gnucash files.
3. Building high quality integration tests with high coverage

The next phase was fortifying because I was making significant
investement in coding effort based on the belief that the resultant
code would be used long term, possibly permenantly.

This phase consisted of build a "flow" component that collected all the "buisnes" logic into
a sequencer that would lend itself well to a "wizard" style UI, such that provided the UI 
with advice on what user interaction was required for the next step, including details on
specifics. Comprehensive test coverage for the sequences was developed.

With the new "flow" feature developed to a high standard, the UI re-work also looked
like settling in a new place more than building up existing structure. Some code
elements were retained for convenience, but really this was another "settling" phase for
the UI. 

The example project currently sits at this state. Note that part of the project is at the "settling" 
phase but part of it is at the next, fortifying stage. 


 

