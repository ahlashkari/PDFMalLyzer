# PDFMalLyzer
This program extracts 30 different features from a set of pdf files specified by the user and wrires them on a csv file. The resulting csv file can be further studied for variety of purposes, most importantly detecting for detecting malicious pdf files.

## Acknowledgement

This project has been made possible through the Lockheed Martin Cybersecurity Research Fund (LMCRF) – from September 2020 to December 2021.

## Modules

pdf_feature_extractor.py is the main module which is extracts a set of general and structural features. It utilizes the fitz library and the pdfid open source python tool.


## Prerequisites
This program runs on Linux operating systems only. It also requires an installation of python3 along with the fitz library.
In order to run the program, navigate to the directory where the pdf_feature_extractor is. Then run the following command in the cmd. The first argument must be the path of a folder containing a set of pdf files.

`python3 pdf_feature_extractor.py pdf-folder-path`

In case the libraries are not installed use the following commands to install them
`pip install fitz`
`pip install PyMuPDF`



## Copyright (c) 2021 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (DoHLyzer), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 
For citation in your works and also understanding DoHLyzer completely, you can find below published paper:
???????????????

## Project Team members

* [**Arash Habibi Lashkari:**](https://www.cs.unb.ca/~alashkar/) Founder and Project Leader
* [**MaryamIssakhani:**] Research and Development (MCS Student)
* [**PrincyVictor:**] Research (PhD Student)

