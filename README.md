# Breez 

## Open Source, kOS Based, Transpiled (or Compiled) Language

```js
print("Breez: The Open Source, kOS Based, Transpiled (or Compiled) Language. For Kerbal Space Nerds");
global interested => true;

while interested = true {
  download();
}
```

Welcome to the Breez Github page, we are a team of developers working on a transpiled language for kOS named Breez. 
Breez will be used in many places like [Saturn Aerospace](https://www.youtube.com/c/SaturnAerospaceKSP), personal projects and other virtual space companies.

If you'd like to start programming rockets with Breez, then [**download it**](https://github.com/KSP-Breez/Breez/releases/latest)!

### Please Note: 
***The transpiled code may be around 2 to 5 times bigger than Breez code.***

***
## What Is Breez?

Breez is a [transpiled](https://medium.com/madfish-solutions/what-is-a-transpiler-47beac592848) language which is transformed into [Kerboscript](http://ksp-kos.github.io/KOS_DOC).
You can use Breez to program rockets in KSP, and then run it through the kOS mod after compiling the code through Yamal (name for our compiler).
 We describe it as: *a stripped down version of Kerboscript that makes syntax more lightweight and also makes kOS more user/programmer friendly.*

***
## What is different?
Due to kOS being very [verbose](https://www.bing.com/search?q=verbose+meaning&cvid=7604b27f4fa7431c90ec9d1e17405cb4&pglt=171&FORM=ANNTA1&PC=U531), we have taken away all of the
useless parts and shortened it all down. 
For example, if you were to be declaring a variable in kOS, it would look like this:

```swift
set variable to 0.
```

However with Breez you only need to write this:

```python
global variable => 0;
```

This makes the code more like more common programming languages like Python or JavaScript, however there are many different bits from other popular languages.

Some noticeable changes from kOS to Breez are: 
* `hold()` - We've changed *wait* to *hold* to add more of a countdown effect.
* `throttle(0.5)` - You now change the throttle by simply calling it like a function!
* `@import:` - Similar to Obj-C/C++, you now *import* rather than doing *runPath* etc.
* `||` - You now type these two lines to basically say *or*.
* `clear();` - This is what *clearscreen* does in kOS.
* Case-sensitivity - You now cannot type in FUNC and fuNC without getting a syntax error.

Obviously there are many more features, however you can experiment with those yourself! 

***
## A Basic Example Program

We're going to demonstrate how different kOS is from Breez below by showing a short example of a KSP rocket scientists first script.

```python
# This is the Breez code:
clear();

global helloText => "Hello World";
print(helloText);

stage();
throttle(1);
print("Ascending");
```
```swift
// This is the kOS code:
clearscreen.

set helloText to "Hello World".
print helloText.

stage.
lock throttle to 1.
print "Ascending".
```

As you can see, there is a significant difference between the two examples.
***
