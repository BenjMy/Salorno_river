echo 'Salerno'

python main.py -Location Salorno -TestName SALORNO1 -recErr 5 -run_indiv 1

python main.py -Location Salorno -TestName SALORNO1 -recErr 5 -TLreg 1 -run_indiv 0
python main.py -Location Salerno -TestName SALORNO2 -recErr 5 -TLreg 1 -run_indiv 0


echo 'Laghetti'

python main.py -Location Laghetti -TestName LAGHETTI1 -recErr 5 -run_indiv 1
python main.py -Location Laghetti -TestName LAGHETTI2 -recErr 5 -run_indiv 1
python main.py -Location Laghetti -TestName LAGHETTI3 -recErr 5 -run_indiv 1

python main.py -Location Laghetti -TestName LAGHETTI1 -recErr 5 -TLreg 1 -run_indiv 0
python main.py -Location Laghetti -TestName LAGHETTI2 -recErr 5 -TLreg 1 -run_indiv 0
python main.py -Location Laghetti -TestName LAGHETTI3 -recErr 5 -TLreg 1 -run_indiv 0

