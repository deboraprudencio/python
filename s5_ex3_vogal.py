def vogal(x):
    char = x.lower()
    if (char == "a") or (char == "e") or (char == "i") or (char == "o") or (char == "u"):
        return True
    else: return False

def test_a():
    assert vogal('a') == True

def test_b():
    assert vogal('b') == False

def test_c():
    assert vogal('c') == False

def test_d():
    assert vogal('d') == False

def test_e():
    assert vogal('e') == True

def test_f():
    assert vogal('f') == False

def test_g():
    assert vogal('g') == False

def test_h():
    assert vogal('h') == False

def test_i():
    assert vogal('i') == True

def test_j():
    assert vogal('j') == False

def test_k():
    assert vogal('k') == False

def test_l():
    assert vogal('l') == False

def test_m():
    assert vogal('m') == False

def test_n():
    assert vogal('n') == False

def test_o():
    assert vogal('o') == True

def test_p():
    assert vogal('p') == False

def test_q():
    assert vogal('q') == False

def test_r():
    assert vogal('r') == False

def test_s():
    assert vogal('s') == False

def test_t():
    assert vogal('t') == False

def test_u():
    assert vogal('u') == True

def test_v():
    assert vogal('v') == False

def test_w():
    assert vogal('w') == False

def test_x():
    assert vogal('x') == False

def test_y():
    assert vogal('y') == False

def test_z():
    assert vogal('z') == False
