@echo off
setlocal

for /f "tokens=*" %%a in (topics.txt) do (type nul>"%%a.dita")

for /f "tokens=*" %%a in (topics.txt) do (
  echo ^<?xml version="1.0" encoding="UTF-8"?^> >>"%%a.dita"
  echo ^<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" "concept.dtd"^> >>"%%a.dita"
  echo ^<concept id="%%a"^> >>"%%a.dita"
  echo ^<title^>^</title^> >>"%%a.dita"
  echo ^<shortdesc^>^</shortdesc^> >>"%%a.dita"
  echo ^<conbody^> >>"%%a.dita"
  echo ^<p^>^</p^> >>"%%a.dita"
  echo ^</conbody^> >>"%%a.dita"
  echo ^</concept^> >>"%%a.dita"
)