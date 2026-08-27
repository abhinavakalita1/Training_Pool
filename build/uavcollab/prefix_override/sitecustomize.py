import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/media/divy/2454fe4a-d2e4-460e-b4f5-df3cde6b9592/training_pool/install/uavcollab'
