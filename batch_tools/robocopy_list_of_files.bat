FOR /F %I IN (TP_docs.txt) DO robocopy \\tycofs.com\gbs\ResearchDevelopment\TechComms\Simplex_FPP_Share\simplex-fire_pdf_crawl \\tycofs.com\gbs\ResearchDevelopment\TechComms\Simplex_FPP_Share\Simplex_TP_PDF_only %I \LOG:copy_log.txt

REM works at cmd line directly, think the /F swithc needs to be replaced in a bat file