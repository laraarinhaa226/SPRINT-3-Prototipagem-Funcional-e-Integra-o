import time

class LcdI2C:
    def __init__(self, i2c, addr=0x27, cols=16, rows=2):
        self.i2c = i2c
        self.addr = addr
        self.cols = cols
        self.rows = rows
        self.bl = 0x08  
        time.sleep_ms(50)
        self._write4(0x30)
        time.sleep_ms(5)
        self._write4(0x30)
        time.sleep_ms(1)
        self._write4(0x30)
        self._write4(0x20)  
        self.cmd(0x28)     
        self.cmd(0x0C)     
        self.cmd(0x06)      
        self.clear()

    def _expander(self, data):
        self.i2c.writeto(self.addr, bytes([data | self.bl]))

    def _write4(self, data):
        self._expander(data)
        self._expander(data | 0x04)  
        time.sleep_us(50)
        self._expander(data & ~0x04)
        time.sleep_us(50)

    def _send(self, value, rs):
        self._write4((value & 0xF0) | rs)
        self._write4(((value << 4) & 0xF0) | rs)

    def cmd(self, c):
        self._send(c, 0)
        if c < 4:
            time.sleep_ms(2)

    def clear(self):
        self.cmd(0x01)

    def move_to(self, col, row):
        self.cmd(0x80 | (col + (0x40 if row else 0)))

    def putstr(self, texto):
        for ch in texto:
            self._send(ord(ch), 1)

    def linha(self, row, texto):
       
        self.move_to(0, row)
        self.putstr((texto + " " * self.cols)[:self.cols])