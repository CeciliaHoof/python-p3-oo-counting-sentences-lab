#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
    self.value = value
  
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, new_value):
    if type(new_value) == str:
      self._value = new_value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    if self.value[len(self.value) - 1] == ".":
      return True
    else:
      return False
    
  def is_question(self):
    if self.value[len(self.value) - 1] == "?":
      return True
    else:
      return False
  
  def is_exclamation(self):
    if self.value[len(self.value) - 1] == "!":
      return True
    else:
      return False
  
  def count_sentences(self):
    no_exclaim = self.value.replace('!', '.')
    new_string = no_exclaim.replace('?', '.')
    sent_list = new_string.split('.')
    list_no_spaces = [sentence for sentence in sent_list if sentence != ""]
    return len(list_no_spaces)


string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
string.count_sentences()