# Screenshot2Code (S2C) - OCR Optimized for Code Screenshots!

**In a nutshell**:  
Use Screenshot2Code to convert code screenshots to text while preserving its format and steering clear of clipboard limitations!

Say you're in any one of these scenarios:  
(1) Your friend sends you a code screenshot message, but you want the code instead.  
(2) The educational website you're looking at uses code images instead of code.  
(3) The reference website you're using doesn't allow for copying text to your clipboard.  
(4) You're taking notes for a programming class and you take a screenshot of code in a YouTube tutorial.  
(5) The code you're looking at is too long to copy and paste to your clipboard.  
(6) The code you copied to your clipboard was overwritten by a more recent copy.  
(7) The CS textbook you're reading is a scanned PDF file that doesn't allow copy-paste.  

Whatever the case, there are many situations where you'll end up with screenshots rather than source code!  
You have three options:  
(1) **Typing it out**: Type out the entire content of the screenshot, taking a bunch of time.  
(2) **Using Conventional OCR**: Convert code into text, and then fix the format errors.  
(3) **Using Screenshot2Code**: Optimized for code screenshots in the most common programming languages.  

To save time and maintain format, you may choose 3!

> Note: this project is currently in ideation stage.

## The Basics of Copy-Paste
Copy-pasting code is done all the time for a plethora of purposes!
1. **Code Generation**: Whether it's CoPilot, ChatGPT, or any other code generation platform, it's now very often the case that you'll need to copy and paste code from these generators into your IDE.
2. **Code from Websites** such as StackOverflow can be copied and pasted into your IDE, or vice versa.
3. **Collaborating**: When collaborating on a project with other developers, it may be necessary to copy and paste code snippets or entire functions to share them with other team members. This can be a quick and easy way to share code and collaborate effectively. But sending code through textual messages on social media can cause you to run into many problems, so people often send screenshots instead.
4. **Reusing code**: Copy and paste code from an existing project or codebase to reuse it in a new project. This can save time and effort and also ensure consistency across projects.
5. **Learning and experimenting**: When learning a new programming language or technology, a developer might copy and paste code snippets from tutorials or forums to experiment with and understand how things work. This can help the developer learn faster and make progress more efficiently.

Whatever the case, there are several common problems you may run into.

## The Problem with Copy-Paste
1. **Formatting issues**: When copying and pasting code between different text editors or programs, the formatting of the code can sometimes get messed up. This can include issues with line breaks, indentation, and spacing, which can make the code difficult to read and understand.
2. **Encoding issues**: Different text editors and programs often use different character encodings, which can cause problems when copying and pasting code between them. This can result in issues with special characters or non-ASCII characters, which can be problematic in internationalization and localization contexts.
3. **Clipboard size limitations**: Some operating systems may have limitations on the size of the clipboard, which can prevent large blocks of code from being copied and pasted.
4. **Clipboard interference**: Other applications can interfere with the clipboard, causing copied text to be lost or overwritten.

**Screenshots, on the other hand, preserve all the information, regardless of origin.**




## Screenshot2Code vs. Existing Methods

#### Conventional Copy-Paste
> Show visual (.gif) of copying/pasting code across two platforms that causes loss of information.

#### Conventional OCR
> Show 2 screenshots, one showing the input image and one showing the misformatted output text.

#### Screenshot2Code
> Show visual (.gif) of Screenshot2Code converting screenshot into formatted code.

Why is Screenshot2Code needed?
- Existing frameworks, libraries, and APIs tend to fall into one of two categories: (1) proprietary and closed-source or (2) open-source but designed for images and not particularly code.
- Generative AI - why not just ask AGI to do it?
  - **GPT-4** can handle image modalities, but it is not accessible to everyone and it is not specialized for this purpose
  - **ChatGPT** does not accept image input.
  - **Google Bard** as of its initial release cannot handle image modalities.
  - **Github CoPilot** cannot handle image modalities.
  - **Codex** cannot handle image modalities.

To the best of our knowledge, there are currently no open-source repositories or APIs that are specifically designed for converting a screenshot into code in a way that preserves syntactical information such as spacing, indentation, and newlines. While there are many OCR and ML tools that can recognize text and generate text from images such as OpenCV or [Pytesseract](https://github.com/madmaze/pytesseract), these tools are not specifically designed for code recognition and may not be able to preserve formatting and syntax information to the extent required for complex code.




## Technical

### Screenshot Formats
Screenshots almost always come in one of two formats depending on the OS.
- **macOS**, **Ubuntu**, and other Linux-based OS's: .png
- **Windows**: .jpg, .jpeg

### Languages we Support
We plan to support some of the most common languages such as:
- Python: .py
- C: .c
- C++: .cpp, .cc, .cxx, .hpp, .h, .hxx
- Java: .java
- JavaScript: .js
- PHP: .php
- Swift: .swift
- Ruby: .rb
- Objective-C: .m
- Kotlin: .kt
- Go: .go
- Rust: .rs
- Perl: .pl
- Shell: .sh
- SQL: .sql
- HTML: .html, .htm
- CSS: .css
- XML: .xml
If there are other languages you would like to be added, please contact us!

#### Authorship
This project is led by [Seth Harding](https://linkedin.com/in/SethHasi).  
For more information or to find out how to contribute to Screenshot2Code, please send an email! seth@dxdr.ai
