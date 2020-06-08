
### Grader Daniel Remarks June 4th 
Nikal, you are overwriting the entire list in create_mimic_dict() when you assign to an existing key (line 58). The idea is to add the word to the existing list instead of reassigning it completely.

Also, in print_mimic(), whenever the last word of the text is chosen as your next current_mimic, a KeyError happens. There is a reason for this. When that happens, you'll want to use the empty string, "", as your next key so that the program can loop back to the beginning of the mimic_dict and continue until it finishes its 200 iterations.

1. I believe I fixed create_mimic