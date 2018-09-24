Question:
  Byomkesh : Ajit babu, are you game to solve a challenge ? 
  Ajit : Do I have a choice ? 
  Byomkesh : Ha, ha, hah. Do not feel so resigned. Challenges are good for the little grey cells as Hercule Poirot would say. 
  Ajit : I am no Hercule Poirot. Or Byomkesh Bakshi for that matter. 
  Byomkesh : Yes. yes. You are the one and only Ajit Kumar Mitra ! 
  Ajit : Ok. Let us hear your challenge. 
  Byomkesh : I have this string of characters. The string has only two types of characters - either 'A' or 'B'. 
  They can be repeated any number of times. I need to find out if the string has equal number of 'A's and 'B's or not. 
  Ajit : This is easy for a change ! Just iterate through the string, count the number of each character and compare at the end. 
  Byomkesh : Not so fast my friend. There are constraints. 
  Ajit : Of course. Nothing comes without constraints. 
  Byomkesh : You cannot use a counter. Nor can you find out the length of the string. 
  Ajit : Now that is a challenge.
  Byomkesh : Question is can you solve it ? 
  
  Write a clear description of how you would help Ajit solve this challenge. Code is not needed for this challenge. 
  Please use clear language to articulate the steps/methods that would be used to arrive at the final answer.

Solution:
  -	Initialize numOfAs = 0
  -	Till end of string, get next character.
      o	  If “A” comes increment value of numOfAs by 1 else if “B” comes decrement value of numOfAs by 1
  -	At the end if value of numOfAs is 0 then both “A” and “B” are in equal number else not equal.
