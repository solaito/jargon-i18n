.. _Obfuscated-C-Contest:

============================================================
Obfuscated C Contest
============================================================

n\.

(in full, the ‘International Obfuscated C Code Contest’, or IOCCC) An annual contest run since 1984 over Usenet by Landon Curt Noll and friends.
The overall winner is whoever produces the most unreadable, creative, and bizarre (but working) C program; various other prizes are awarded at the judges' whim.
C's terse syntax and macro-preprocessor facilities give contestants a lot of maneuvering room.
The winning programs often manage to be simultaneously (a) funny, (b) breathtaking works of art, and (c) horrible examples of how *not* to code in C.

This relatively short and sweet entry might help convey the flavor of obfuscated C:

.. code-block:: none


   /*
    * HELLO WORLD program
    * by Jack Applin and Robert Heckendorn, 1985
    * (Note: depends on being able to modify elements of argv[],
    * which is not guaranteed by ANSI and often not possible.)
    */
   main(v,c)char**c;{for(v[c++]="Hello, world!\n)";
   (!!c)[*c]&&(v--||--c&&execlp(*c,*c,c[!!c]+!!c,!c));
   **c=!c)write(!!*c,*c,!!**c);}

Here's another good one:

.. code-block:: none


   /*
    * Program to compute an approximation of pi
    * by Brian Westley, 1988
    * (requires pcc macro concatenation; try gcc -traditional-cpp)
    */

   #define _ -F<00||--F-OO--;
   int F=00,OO=00;
   main(){F_OO();printf("%1.3f\n",4.*-F/OO/OO);}F_OO()
   {
               _-_-_-_
          _-_-_-_-_-_-_-_-_
       _-_-_-_-_-_-_-_-_-_-_-_
     _-_-_-_-_-_-_-_-_-_-_-_-_-_
    _-_-_-_-_-_-_-_-_-_-_-_-_-_-_
    _-_-_-_-_-_-_-_-_-_-_-_-_-_-_
   _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
   _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
   _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
   _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
    _-_-_-_-_-_-_-_-_-_-_-_-_-_-_
    _-_-_-_-_-_-_-_-_-_-_-_-_-_-_
     _-_-_-_-_-_-_-_-_-_-_-_-_-_
       _-_-_-_-_-_-_-_-_-_-_-_
           _-_-_-_-_-_-_-_
               _-_-_-_
   }

Note that this program works by computing its own area.
For more digits, write a bigger program.
See also :ref:`hello-world`\.

The IOCCC has an official home page at `http://www.ioccc.org/ <http://www.ioccc.org/>`_.

