
# Control Flow: Conditionals - Lab

## Introduction
Now that we have been introduced to some difference data types, how to use them, and now conditionals, let's put our knowledge to the test and create some conditional statements that selectively assign values to variables based on whether they pass a certain condition of ours.

## Objectives
* Understand and use conditionals

## Instructions

Let's use our knowledge of variables and conditionals to assign values based on different conditions. Follow the instructions below to properly assign the values.

Below, use conditionals to tell whether it is hot outside or not. If it is hot, assign the string `"It is so hot out!"` to the variable `is_it_hot`. If it is not hot, assign the string `"This is nothing! Bring on the heat."`. For our purposes, anything over `80` degrees is considered hot.


```python
temperature = 85
is_it_hot = None
# conditionals go here
```

Next, let's see what day of the week it is. There are 7 days in the week starting with Sunday at day `1` and ending with Saturday at day `7`. Use conditional statements to assign the day of the week to the variable `day_of_the_week` based on the number below assigned to the variable `today_is`.
For example, if the day is `2`, we would assign `day_of_the_week` the value `"Monday"`.


```python
today_is = 4
day_of_the_week = None
# conditionals go here
```

Next, let's take a string and see if it ends with a certain substring. If it does, assign the variable `ends_with` to either `True` or `False`. For example, we have the string "School" and we want to know if it ends with the sub-string "cool". In this case it does not, so, we would assign `False` to the variable `ends_with`. 


```python
string = "Python"
sub_string = "on"
ends_with = None
# conditionals go here
```

Finally, we will compare two numbers and save the Boolean returned in the variable `result`. Use the value from the result to assign the `bigger_number` variable the number that is bigger. So, if `10` is bigger than 5, then assign `bigger_number` the value `10`. Pretty straight forward, right?


```python
result = 10 > 5
bigger_number = None
# conditionals go here
```

### Summary

Great! In this lab we saw how to use our knowedge of conditionals to selectively assign values based on a condition. We will start integrating conditionals in many more ways in our code and we will start to see how useful they can become in more complex problems.
