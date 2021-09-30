# dashboard-api

This python program generates a resume from the user input data. The program uses report lab library. 
Profile, education, trainings, projects, experience,skills, hobbies. Apart from this, user can also add section of his/her choice.

Use of custom font has been made - Century Gothic and Century Gothic Bold. .ttf files have been uploaded in the repository as well. Make sure the font files (.ttf) and program is in same directory.
The program gives following section choices to the user - 


The program following three functions/modules

1) main - main function is responsible for passing the JSON data generated from user input( 2 dictionaries - 1.contact_info and 2. professional_info) to other functions -  pdf_serializer and pdf_first_page_header.

2) pdf_first_page_header - prints user name in bold on the first page of the pdf only.

3) pdf_serializer - generates the resume from JSON data.

#The steps to run the program are as follows:-

1) Download the source code from the repository.
2) Now, put the fonts(.ttf) files and the python program(.py) in the same folder/directory.
3) Run the program using suitable python IDE.
4) The resume (in PDF format) will be generated and saved in the same directory as program and font files.
