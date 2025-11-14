#!/usr/bin/env python3
from pathlib import Path
from subprocess import Popen

top = Path(__file__).parent.parent
dirs = [
    top / "partials" / "general",
    top / "partials" / "modes",
    top / "partials" / "phases",
    top / "partials" / "roles",
    top / "iterations" / "pass_2",
]
for tdir in dirs:
    for sfile in tdir.glob("*.org"):
        command = [ 'pandoc', '--wrap=none',
                    '-s', '-f', 'org', '-t', 'markdown+yaml_metadata_block', sfile, '-o', f"{sfile.with_suffix('.md')}"]
        print(command)
        p = Popen(command)
        print(p.communicate())
        
