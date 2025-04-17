# 303_Spring_25.

Code Review Issues: team_ex_2.py

Tasks & Assignments 

Refactored Code (meeting all new functionality requirements)

Issues Identified

Issue #	Description
* Code is repetitive across functions (dl_and_save, dl_and_save_thread, dl_and_save_process). DRY principle violated.
  
* Nested functions in wiki_sequentially and concurrent_threads prevent reuse and aren't supported by multiprocessing.
  
* No input handling for custom search terms and fallback default term.
  
* Output files saved in the current directory; doesn't meet the requirement to save in a "wiki_dl" directory.
  
* Error handling is missing in dl_and_save_* functions — a bad page will crash the program.


Tasks and Assignments

Stephen - Move dl_and_save to global scope with error handling
Solution: Create dl_and_save(item, outdir)


Rhett - Create wiki_dl/ directory if not exists	and add input prompt with fallback to default term	
Solution: Use os.makedirs("wiki_dl", exist_ok=True)
          Use input() with length check 

Tracy - Apply DRY principle for filename + writing logic
Solution: Reuse convert_to_str

Charlize - Document code with inline comments and run & test all implementations	
Solution: Add docstrings and comments

Rohini: Create README or markdown report and push working version to GitHub
Solutions: Document issues, fixes, results	
Verify file/folder structure in repo
