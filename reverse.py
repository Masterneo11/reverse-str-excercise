# make  a function that takes in a string and returns a reversed copy 
import pytest

a = "hey"
def reverse(a) -> str:
    reversel = []
    for i in a:
        reversel.append(i)
    reversel = reversel[:: -1]
    rv = ''.join(reversel)
    return rv

print(reverse(a))



def test_reverse():
    assert reverse("ab") == "ba"
    assert reverse("beautiful") == "lufituaeb"
    assert reverse("") == ""

test_reverse()
