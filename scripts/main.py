#!/usr/bin/env python3
import argparse
from guardrails.dataservice import DataService



if __name__ in {"__main__", "__mp_main__"}:

    parser = argparse.ArgumentParser(description='Guardrails Commander')

    op_group = parser.add_mutually_exclusive_group(required=True)
    op_group.add_argument('-q', '--generate-questions', action='store_true',
                       help="Produce a JSON doc detailing the question pattern")
    op_group.add_argument('-a', '--save-answers', type=str,
                       help="Load JSON QandA file and produce a process_doc")
    doc_group = parser.add_mutually_exclusive_group(required=True)
    doc_group.add_argument('-s', '--story', type=str, default="study",
                            help="Make a story of given type: study | pathfinder | forming | compliance | user ")
    doc_group.add_argument('-t', '--task', type=str, 
                            help="Using provided story QandA file, make a task of given type")

    args = parser.parse_args()
    main()
