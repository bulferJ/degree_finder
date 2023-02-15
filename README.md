Scholarwise 

The current main.py is the first bit of code I wrote for this program as an example. There is much more which 
will be released as well as extensive documentation. There are no comments in the example code but you will 
undertand it upon further reading of this file. 

Here are bits and pieces from several documentation files, as well as an explanation from a resume of mine. The 
following descriptions will be disorganized and uncomplete, but you will get the idea.


definitions:

    entity - my own word for this program which will include degrees, 
    certificates and minors. The entity class will be created from
    the degrees, certificates, bachelor, etc. classes will inherit from. 
    However, the word entity will also be used in non-technical terms as 
    I could find no convenient term which describes certificates, '
    degrees, and other "objects" which will be included in the program. 



https://catalog.dsu.edu/preview_program.php?catoid=35&poid=2669&returnto=1625
                                                           ^^^^  
This sample url is the first web page in a list which starts at 2669 and ends at 2787, for
a total of 118 pages that describe each entity, which I defined above. This exact url describes 
the Digital Art Design Bachelor Degree, with continued web pages
in the list describing each entity which can be awarded at DSU. Most prominently listed 
on each webpage is the required classes and respective credits awarded for each, as well as
the total credits required to be awarded the degree. 



Non-Technical Description 

 

This Python software, which I have named Scholarwise is a tool that aids students in determining which degrees, majors, minors, and certificates to pursue in college. It receives input from the student regarding their academic goals and potential scenarios, such as working towards a Network Administration Associate degree and coding certificate.  

 

Using a comprehensive database of all degrees, minors, and certificates available, the program identifies overlapping courses that the student has already completed for other similar degrees and certificates. The program then generates a report listing every degree, minor, and certificate which the student has already partially completed, helping them make the most informed decision.  

 

Furthermore, the program identifies similar minors, associate degrees, and other related paths the student could pursue based on their current academic status. It also presents students with different future scenarios to consider, based on their academic goals and the courses they have already taken.  

 

This program provides a valuable tool for students to save time and money while pursuing their academic goals, providing valuable insights to students and helping them make informed decisions about their future academic careers.  







This (see main.py) extracts the HTML “soup”, or the entire code, which makes up the DSU website. The program will find the webpages of the course catalog, associated with each degree and certificate, and scrape relevant data, such as the course names, class codes, and credits awarded. For future development I will likely extract this data somewhere more reliable such as the South Dakota Board of Regents to maintain data integrity. This is because the website may not always be up to date, or the HTML source code may be updated or modified over time. 

After scraping HTML tags, such as “<a> CSC 234 - Software Security</a> “3 Credits” ”, the regex will divide each of these tags into three separate variables, class_name, class_code, and class_credits respectively. This example code then prints these variables onto the screen for the programmer to ensure it was extracted and parsed without error. 



![image](https://user-images.githubusercontent.com/117784062/218905634-859d71fc-b7b8-47ab-b40d-be22757d6c9c.png)
