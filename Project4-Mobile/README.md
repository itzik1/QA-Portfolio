Testing user experience on mobile devices using Chrome DevTools.
# Project 4 – Mobile Responsiveness Testing

## Description
This project focuses on testing the mobile responsiveness of a web application using browser developer tools (for example: Chrome DevTools).  
The goal is to ensure a good user experience on different screen sizes and devices.

## Devices / Viewports Tested
- iPhone 12 (portrait)  
- Galaxy S20 (portrait)  
- Generic small-screen Android  

## Test Scenarios (Examples)

### Scenario 1 – Navigation Menu (Hamburger)

**Steps:**
1. Open the site in mobile view (iPhone 12).  
2. Tap the hamburger menu icon.  

**Expected Result:**
- The menu opens smoothly and all menu items are visible.

**Actual Issues Found (Example):**
- Menu animation is delayed.  
- Some menu items are partially cut off.

---

### Scenario 2 – Keyboard Covering Input Field

**Steps:**
1. Open a form with input fields.  
2. Tap on the bottom input field.  
3. The on-screen keyboard opens.

**Expected Result:**
- The screen scrolls so that the input field remains fully visible.

**Actual Issues Found (Example):**
- The input field is partially covered by the keyboard.

### Scenario 3 – Layout Overflow
**Steps:**
1. Navigate to a page with cards or tiles.  
2. Test on Galaxy S20 resolution.  

**Expected Result:**
- No horizontal scrolling is needed.  
- Cards are aligned correctly.

**Actual Issues Found (Example):**
- One card overflows outside the screen on small devices.

## Conclusion
This project demonstrates the ability to:
- Use browser dev tools for mobile simulation  
- Identify UI and UX issues  
- Report layout and usability problems clearly
