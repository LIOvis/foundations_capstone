# foundations_capstone
foundations capstone repository

    This application is to be used to keep track of:
        * Competencies
        * Assessments of those Competencies
        * Users who will take those Assessments
        * Competency Assessment Results of those Users

        Competencies:
            * Competency ID as a Unique Identifier in the Database
            * Name of the Competency
            * Description of the Competency

        Assessments:
            * Assessment ID as a Unique Identifier in the Database
            * Comptency ID Referencing Which Competency the Assessment Relates to
            * Name of the Assessment
            * Date the Assessment Was Created 

        Users:
            * User ID as a Unique Identifier in the Database
            * First Name of the User
            * Last Name of the User
            * Phone Number of the User
            * Email of the User - Used With the User's Password to Log In
            * Password of the User - Used With the User's Email to Log In
            * Hire Date of the User
            * Date the User's Record Was Created
            * Role of the User - User or Admin
            * Active Status of the User

        Competency Assessment Results:
            * Result ID as a Unique Identifier in the Database
            * User ID of the User Who Took the Assessment
            * Assessment ID of the Assessment Taken
            * Score of the Assessment - 0 Through 4
            * Date the Assessment Was Taken
            * Admin ID - User ID of the Admin Who Proctored the Assessment

        
    Please make sure to enter 'pipenv shell' into the terminal if bcrypt raises an error.

    Check 'test_logins.txt' to find both Admin and User login information for testing.

    Admin Instructions:
        
        Logging In:
            Enter your active Admin email and password.
        
        Viewing Records:
            Enter 1 for (1) View Records at the Main Menu
            
                Enter 1 for (1) View Users
                
                    Enter 1 for (1) View All Users
                    Enter 2 for (2) View All Active Users
                    Enter 3 for (3) View All Inactive Users:
                    
                        Enter a User ID to View a Specific User 
                        or
                        Press 'Enter' to Return to Main Menu

                Enter 2 for (2) View Competencies:
                    Enter a Competency ID to View a Specific Competency 
                    or
                    Press 'Enter' to Return to Main Menu

                Enter 3 for (3) View Assessments:
                    Enter an Assessment ID to View a Specific Assessment 
                    or
                    Press 'Enter' to Return to Main Menu

                Enter 4 for (4) View Competency Assessment Results:
                    Enter a Result ID to View a Specific Result 
                    or
                    Press 'Enter' to Return to Main Menu

                Enter 5 for (5) Return to Main Menu

        Creating Records:
            Enter 2 for (2) Create Records at the Main Menu
            
                Enter 1 for (1) Create New User
                    Enter Information for All Fields When Prompted
                        Last Name is not a Required Field 
                        
                        Phone is not a Required Field 
                        
                        Hire Date is not a Required Field - Will Default to Current Date
                        
                        Date Created is not a Required Field - Will Default to Current Date
                        
                        Active is not a Required Field - Null Will Read as Inactive

                Enter 2 for (2) Create New Competency
                    Enter Information for All Fields When Prompted            
                        Description is not a Required Field

                Enter 3 for (3) Create New Assessment
                    Enter Information for All Fields When Prompted
                        If Date Created is Left Empty it Will Default to Current Date   

                Enter 4 for (4) Create New Competency Assessment Result
                    Enter Information for All Fields When Prompted
                        If Date Taken is Left Empty it Will Default to Current Date

                        Admin ID is not a Required Field

                Enter 5 for (5) Return to Main Menu

        Editing Records:
            Enter 3 for (3) Edit Records at the Main Menu

            Enter 1 for (1) Edit a User:
                Enter the User ID of the User You Wish to Edit
                    Enter 0 for (0) User ID: <user_id>
                        Enter Updated Information for Field When Prompted
                        Must Not be Null
                        Must be Unique
                    Enter 1 for (1) First Name: <first_name>
                        Enter Updated Information for Field When Prompted
                        Must Not be Null
                    Enter 2 for (2) Last Name: <last_name>
                        Enter Updated Information for Field When Prompted
                        May be Null
                    Enter 3 for (3) Phone: <phone>
                        Enter Updated Information for Field When Prompted
                        May be Null
                    Enter 4 for (4) Email: <email>
                        Enter Updated Information for Field When Prompted
                        Must Not be Null
                        Must be Unique
                    Enter 5 for (5) Password
                        Enter Updated Information for Field When Prompted
                        Must Not be Null
                        Must Verify Knowledge of Current Password Before Allowing Change
                    Enter 6 for (6) Hire Date: <hire_date>
                        Enter Updated Information for Field When Prompted
                        May be Null
                    Enter 7 for (7) Date Created: <date_created>
                        Enter Updated Information for Field When Prompted
                        May be Null
                    Enter 8 for (8) Role: <role>
                        Enter Updated Information for Field When Prompted
                    Enter 9 for (9) Active: <yes/no>
                        If User is Active Enter Y When Prompted to Deactivate
                        If User is inactive Enter Y When Prompted to Reactivate

            Enter 2 for (2) Edit a Competency:
                Enter the Competency ID of the Competency You Wish to Edit
                    Enter 1 for (1) Competency ID: <competency_id>
                        Enter Updated Information for Field When Prompted
                        Must Not be Null
                        Must be Unique
                    Enter 2 for (2) Name: <name>
                        Enter Updated Information for Field When Prompted
                        Must Not be Null
                    Enter 3 for (3) Description: <description>
                        Enter Updated Information for Field When Prompted
                        May be Null

            Enter 3 for (3) Edit an Assessment:
                Enter the Assessment ID of the Assessment You Wish to Edit
                    Enter 1 for (1) Assessment ID: <assessment_id>
                        Enter Updated Information for Field When Prompted
                        Must Not be Null
                        Must be Unique
                    Enter 2 for (2) Competency ID: <competency_id>
                        Enter Updated Information for Field When Prompted
                        Must Not be Null
                    Enter 3 for (3) Name: <name>
                        Enter Updated Information for Field When Prompted
                        Must Not be Null
                    Enter 4 for (4) Date Created: <date_created>
                        Enter Updated Information for Field When Prompted
                        Must Not be Null

            Enter 4 for (4) Edit a Competency Assessment Result:
                Enter the Result ID of the Result You Wish to Edit
                    Enter 1 for (1) Result ID: <result_id>
                        Enter Updated Information for Field When Prompted
                        Must Not be Null
                        Must be Unique
                    Enter 2 for (2) User ID: <user_id>
                        Enter Updated Information for Field When Prompted
                        Must Not be Null
                    Enter 3 for (3) Assessment ID: <assessment_id>
                        Enter Updated Information for Field When Prompted
                        Must Not be Null
                    Enter 4 for (4) Score: <score>
                        Enter Updated Information for Field When Prompted
                        Must Not be Null
                    Enter 5 for (5) Date Taken: <date_taken>
                        Enter Updated Information for Field When Prompted
                        Must Not be Null
                    Enter 6 for (6) Admin Id: <admin_id>
                        Enter Updated Information for Field When Prompted
                        May be Null

            Enter 5 for (5) Return to Main Menu:

        Searcing Users:
            Enter 4 for (4) Search Users at Main Menu

                Enter the first OR last name when prompted - not both.

                    Enter a User ID of a User You Would Like to View
                    or
                    Press 'Enter' to Return to Main Menu
        
        Getting Reports:
            Enter 5 for (5) Get Reports at Main Menu

                Enter 1 for (1) Get User Competency Summary:
                    Enter a User ID When Prompted

                Enter 2 for (2) Get Competency Results Summary:
                    Enter a Competency ID When Prompted

                Enter 3 for (3) Return to Main Menu:

        Exporting CSVs:
            Enter 6 for (6) Export CSVs at Main Menu

                Enter 1 for (1) Export User Assessment Results:
                    Enter a User ID When Prompted
                    Enter a Name for the CSV File
                        If a File With That Name Already Exists:
                            Enter Y When Prompted to Overwrite Current File
                            or
                            Enter N When Prompted to Keep Current File
                    Enter Y When Prompted to Export with Result ID
                    or
                    Enter N When Prompted to Export without Result ID

                Enter 2 for (2) Export Competency Assessment Results:
                    Enter a Competency ID When Prompted
                    Enter a Name for the CSV File
                        If a File With That Name Already Exists:
                            Enter Y When Prompted to Overwrite Current File
                            or
                            Enter N When Prompted to Keep Current File
                    Enter Y When Prompted to Export with Result ID
                    or
                    Enter N When Prompted to Export without Result ID

                Enter 3 for (3) Export Users:
                    Enter a Name for the CSV File
                        If a File With That Name Already Exists:
                            Enter Y When Prompted to Overwrite Current File
                            or
                            Enter N When Prompted to Keep Current File
                    Enter Y When Prompted to Export with User ID
                    or
                    Enter N When Prompted to Export without User ID

                Enter 4 for (4) Export Competencies:
                    Enter a Name for the CSV File
                        If a File With That Name Already Exists:
                            Enter Y When Prompted to Overwrite Current File
                            or
                            Enter N When Prompted to Keep Current File
                    Enter Y When Prompted to Export with Competency ID
                    or
                    Enter N When Prompted to Export without Competency ID
                    
                Enter 5 for (5) Export Assessments:
                    Enter a Name for the CSV File
                        If a File With That Name Already Exists:
                            Enter Y When Prompted to Overwrite Current File
                            or
                            Enter N When Prompted to Keep Current File
                    Enter Y When Prompted to Export with Assessment ID
                    or
                    Enter N When Prompted to Export without Assessment ID
                    
                Enter 6 for (6) Return To Main Menu


        Importing CSVs:
            Enter 7 for (7) Import CSVs at Main Menu

                Enter 1 for (1) Import Into Users:
                    Enter the Name of the CSV File You Wish to Import

                Enter 2 for (2) Import Into Competencies:
                    Enter the Name of the CSV File You Wish to Import

                Enter 3 for (3) Import Into Assessments:
                    Enter the Name of the CSV File You Wish to Import

                Enter 4 for (4) Import Into Competency Assessment Results:
                    Enter the Name of the CSV File You Wish to Import

                Enter 5 for (5) Return To Main Menu

        Logging Out:
            Enter 8 for (8) Log Out at Main Menu

                This will log you out without quitting the application.

        Quitting:
            Enter 9 for (9) Quit

                This will log you out before quitting the application.


    User Instructions:

        Viewing Your Profile:
            Enter 1 for (1) View Your Profile

        Editing Your Profile:
            Enter 2 for (2) Edit Your Profile
                Enter 1 for (1) First Name: <first_name>
                    Enter Updated Information for Field When Prompted
                    Must Not be Null
                Enter 2 for (2) Last Name: <last_name>
                    Enter Updated Information for Field When Prompted
                    May be Null
                Enter 3 for (3) Phone: <phone>
                    Enter Updated Information for Field When Prompted
                    May be Null
                Enter 4 for (4) Email: <email>
                    Enter Updated Information for Field When Prompted
                    Must Not be Null
                    Must be Unique
                Enter 5 for (5) Password
                    Enter Updated Information for Field When Prompted
                    Must Not be Null
                    Must Verify Knowledge of Current Password Before Allowing Change

        Viewing Your User Competency Summary:
            Enter 3 for (3) View Your User Competency Summary
                Enter N When Prompted To Return to Main Menu
                or
                Enter Y When Prompted To Export as a CSV
                    Enter a Name for the CSV File
                        If a File With That Name Already Exists:
                            Enter Y When Prompted to Overwrite Current File
                            or
                            Enter N When Prompted to Keep Current File
                    Enter Y When Prompted to Export with Result ID
                    or
                    Enter N When Prompted to Export without Result ID


        Logging Out:
            Enter 4 for (4) Logout

                This will log you out without quitting the application.

        Quitting:
            Enter 5 for (5) Quit
                
                This will log you out before quitting the application.