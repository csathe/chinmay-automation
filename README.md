A to Z guide on how to do web automation using Python and Selenium Webdriver, starting from nothing, including CI.

Important Notes:

* This is very much a work in progress, you will see constant updates and optimizations as I commit new code and write new tests
* Currently its more of a sample, so you will see only a small number of tests demonstrating how to automate and perform operations, by using a
standard well known site - facebook's login page as an example.
* This framework will aid in teaching anyone who wants to learn automation, as it is organized it a very logical, clear and easy to understand fashion.

Framework Organization :

1) runTests.py is the main starting file, that starts running all the tests. It uses Python's unittest framework and calls tests.py

2) tests.py are where the tests are actually written, and assertions are checked. This uses use different classes and modules of the framework.

3) There are 3 store rooms as follows:

elements_store_room - stores ids, xpaths, css selectors etc. recorded from Selenium for different elements.
values_store_room - stores the actual values that you will enter in different boxes, dropdowns, and values used for various asserttion tests.
selectors_store_room - stores different selectors, used to access page elements in combination with ids from the elements_store_room.

All three are used throughout the framework. The advantage of this approach is that whenever developers add new elements, change existing ids, etc.
you dont have to search throughout and make changes at many places. You just have to make the change at one centralized place depending upon what was updated.
Easy to maintain and understand.

4) Different classes execute actual code , return results etc. They use the 3 store_rooms and are in turn used by tests.py


Technical Points:

1) Sometimes the latest version of Selenium does not play well with the latest version of Firefox, since both are releasing code rapidly. So for this demo,
I used a combination that works - latest version of Selenium and an older version of Firefox - Firefox 30.0  (current is 45). This is the quickest way to see this automation in action, but if you have time you can try different Selenium/Firefox combinations. How to downgrade
firefox is on the web.
2) This is using a Python 2.7 interpreter since there were complex issues with python 3.0 bindings in the latest selenium version.

Happy automation !