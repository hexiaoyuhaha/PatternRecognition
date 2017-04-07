# Pattern Recognition

1. Pattern recognition using regular expression
2. Pattern recognition using open source libraries
3. Pattern recognition using third party tools 


##	Open source libraries for Phone Number
We explored one library for phone number detection, we will explore more library for date detection, address detection in the future.

### Google libphonenumber

Google's provides Java, C++ and JavaScript library for parsing, formatting, and validating international phone numbers.  https://github.com/googlei18n/libphonenumberThis library can validate phone number, extract country code and national number, reformat the number, etc. A [quick example](https://github.com/googlei18n/libphonenumber#quick-examples). A [JavaScript Demo](https://rawgit.com/googlei18n/libphonenumber/master/javascript/i18n/phonenumbers/demo-compiled.html)


There are several third-party ports of the phone number library supporting various languages:

*   C#: https://github.com/aidanbebbington/libphonenumber-csharp
*   PHP: https://github.com/giggsey/libphonenumber-for-php
*   Python: https://github.com/daviddrysdale/python-phonenumbers
*   Ruby: https://github.com/sstephenson/global_phone
*   javascript (stripped-down version): https://github.com/halt-hammerzeit/libphonenumber-js
*   objective-c: https://github.com/iziz/libPhoneNumber-iOS

You can try it with your own number. For example, the demo output looks like this:

<img src="images/google-parser-phone.png" width="400"/>
##	Paid third party software

Generally, open source libraries already provide satisfying functionality for daily uses. But if more advanced functionality is required, we’ve found some third party software to provide more sophisticated functionalities. ### TwilioFor example, [Twilio](https://www.twilio.com/lookup) can be used for number detection. It support functionality such as:

- Find Caller Name: Get the Caller ID Name (CNAM) for a phone number
- Identify carrier: Know which carrier is connected to a user's number
- Check type: Determine if a number is a landline, VoIP, or mobile---

