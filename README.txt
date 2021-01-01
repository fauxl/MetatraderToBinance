
This Project uses mq4 so the script works on metatrader 4.

This was meant to connect the MT account with the Binance one, but there were some issues regarding
the possibility of tryng it with real transactions if it really worked. Given the two keys given by Binance, 
the connection works and simulated transactions too; but since it was for a University project i didn't spent money 
to try it out on real transtaction.

So the project focused on translating all open transactions of metatrader on the website
i created with python and flask, and eventually open them also on Binance, that goes also
for all modification of SL and TP. 

But like i said the copy on Binance of real order was not tested.

The communication from binance to python is based on files, at each tic on MT the files update itself
and python reads them constantly updating the orders and the other informations.
