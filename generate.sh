clear
echo "Installing Reqired Pakages"
pkg install toilet
toilet -f bigascii12  	strong password
toilet -f bigascii12    ABHI
sleep  3.0
cd $HOME/generator
python pass.py
