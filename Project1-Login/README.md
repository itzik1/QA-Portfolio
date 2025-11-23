Login testing project with STP, STD, STR and bug reports.
# Project 1 – Web Testing: Login System

## Description
This project focuses on manual testing of a basic login system.  
The goal is to verify correct behavior for valid and invalid login attempts, password recovery, and field validation, as well as to document bugs in a clear and professional way.

## Scope
- Login with valid credentials
- Login with invalid credentials
- Email format validation
- Empty fields behavior
- Forgot Password flow
- Basic cross-browser check (Chrome, Firefox)

## Test Cases (Examples)

**TC01 – Valid Login**  
Steps:  
1. Enter a valid email  
2. Enter a valid password  
3. Click "Login"  

Expected result:  
- User is redirected to the dashboard page.

---

**TC02 – Invalid Password**  
Steps:  
1. Enter a valid email  
2. Enter an incorrect password  
3. Click "Login"  

Expected result:  
- Error message: "Incorrect password" is displayed.  
- User remains on the login page.

---

**TC03 – Invalid Email Format**  
Steps:  
1. Enter "itzikgmail.com" in the email field  
2. Enter a valid password  
3. Click "Login"  

Expected result:  
- Error message: "Invalid email format" is displayed.  

---

**TC04 – Empty Fields**  
Steps:  
1. Leave email and password empty  
2. Click "Login"  

Expected result:  
- Login button remains disabled or an error message is shown indicating that fields are required.

---

**TC05 – Forgot Password Flow**  
Steps:  
1. Click "Forgot Password"  
2. Enter a valid registered email  
3. Submit the form  

Expected result:  
- A password reset email is sent to the user.  

Actual result (found bug):  
- No email is sent.

## Sample Bug Report

**Bug ID:** WEB_LOGIN_001  
**Title:** Password reset email is not sent  
**Severity:** High  
**Priority:** High  
**Environment:** Web, Chrome latest  

**Steps to Reproduce:**
1. Navigate to the login page.  
2. Click on "Forgot Password".  
3. Enter a valid registered email.  
4. Click "Submit".  

**Expected Result:**  
A password reset email is sent to the entered email address.

**Actual Result:**  
No email is received. No error is displayed in the UI.

**Status:** Open  
**Type:** Functional bug
