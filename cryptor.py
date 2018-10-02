'''
Only for ASCII Characters.
'''
import base64

class Cryptor:
    
    def __init__(self, keys):
        '''
        keys: a list of string.
        '''
        self.keys = keys

    def get_byte(self, data):
        tmp = []
        for s in data:
            tmp.append(ord(s))
        return tmp
    
    def get_char(self, byte):
        s = ''
        for n in byte:
            s += chr(n)
        return s

    def encrypt(self, data):
        """
        data: string 
        """
        secret_str = ""
        for key in self.keys:
            tmp_list = []
            data_bytes = self.get_byte(data)
            key_bytes = self.get_byte(key)
            key_length = len(key_bytes)
            for k, v in enumerate(data_bytes):
                tmp_list.append(str((0xFF & v) + (0xFF & key_bytes[k % key_length])))
            secret_str = "@" + "@".join(tmp_list)
            data = str(secret_str)

        b64ed_secret_str = base64.b64encode(secret_str.encode())
        
        return b64ed_secret_str
        

    def decrypt(self, data):
        """
        data: string
        """
        data = data.encode()
        data = base64.b64decode(data)
        reversedkeys = reversed(self.keys)
        try:
            for key in reversedkeys:
                tmp_list = []
                data_bytes = data.split(b'@')
                del(data_bytes[0])
                key_bytes = self.get_byte(key)
                key_length = len(key_bytes)
                for k, v in enumerate(data_bytes):
                    tmp_list.append(int(v) - (0xFF & key_bytes[k % key_length]))
                data = bytes(self.get_char(tmp_list).encode())

            return data
        except:
            return "error"
