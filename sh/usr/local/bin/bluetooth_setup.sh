sudo hcitool scan
sudo hciconfig hci0 up
sudo rfcomm bind 0 00:1D:A5:03:3D:6E
sudo rfcomm listen 0 1 &