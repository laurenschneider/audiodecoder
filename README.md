# Audio Decoder
<H2> Author: Lauren Schneider </H2>
Homework #1 for Computers, Sounds, & Music at Portland State University.
Build an audio decoder using the Bell 103 modem protocol.
</br>
</br>

<p>
  The first thing I did when working on this assignment was attempt to follow the linked Embedded.com article on Goertzel filters. I found this article helpful and simple to follow, but in the end I used the formula examples in the python walkthrough that seemed to match the Wikipedia article more closely. When following the Embedded.com article, I avoided imaginary numbers in my implementation. In fact it is quite simple in Python to calculate <i>i</i>. 
</p>

<p>
  Next, I played with the different libraries available in Python for reading and working with wavefiles. I found SciPy's methods to be straightforward, and only a few lines of code to get the job done. It ran fast enough for the purpose of this project so I was satisfied to use this method for reading the wav file.
</p>
<p>
  Once I got the program to output a result, I noticed it was printing backwards, which I then realized was due to the endianness of the bits. This was a quick fix to reverse the bits in the final string. One thing I struggled with for awhile was that the result was printing the first character of the solution last. Professor Massey pointed out to me that I needed to adjust my loop variables to get the message to print correctly. I still don't have a full understanding as to why this is, so I suppose what is left to be done would be for me to investigate this strange feature of the wav file bits.
</p>

<p>
  Overall, I found this assignment to be a rewarding challenge. Using Python made some things quick and easy and allowed me to focus on the conceptual pieces rather than excessive details in the implementation.
 </p>
