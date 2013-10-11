python tabify.py w1.csv w2.dat
python mrproj.py w2.dat > w3.dat
python mrr.py w3.dat  > R.dat # cholesky R
python mrq.py w3.dat --R=R.dat --file R.dat > Q.dat # get Q
python mraq.py w2.dat Q.dat > BT.dat
python mrr.py BT.dat  > R_BT.dat
python mr_q_uhat.py Q.dat --R=R_BT.dat --file R_BT.dat > U_final.dat
