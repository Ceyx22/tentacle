import numpy        as np

def reye():
    np.eye(3)

def crossmat(e):
    e = e.flatten()
    return np.array([[  0.0, -e[2],   e[1]], 
                     [  e[2],  0.0,  -e[0]], 
                     [ -e[1], e[0],   0.0]])

def pzero():
    return np.zeros((3,1))

def quat(w, i, j, k):
    return np.array([w, i, j, k]).reshape((-1, 1))


def rot_from_quat(quat):
    q       = quat.flatten()
    norm    = np.inner(q, q)
    w       = q[0]
    v       = q[1:].reshape((3,1))
    r = (2/norm)*(v @ v.T + w*w*reye() + w*crossmat(v)) - reye()
    return r

def quat_from_rot(rot):
    A = [1.0 + rot[0][0] + rot[1][1] + rot[2][2], 
         1.0 + rot[0][0] - rot[1][1] - rot[2][2],
         1.0 - rot[0][0] + rot[1][1] - rot[2][2],
         1.0 - rot[0][0] - rot[1][1] + rot[2][2],]
    i = A.index(max(A))
    A = A[i]
    c = 0.5/np.sqrt(A)
    if   (i == 0):
        q = c*np.array([A, rot[2][1]-rot[1][2], rot[0][2]-rot[2][0], rot[1][0]-rot[0][1]])
    elif (i == 1):
        q = c*np.array([rot[2][1]-rot[1][2], A, rot[1][0]+rot[0][1], rot[0][2]+rot[2][0]])
    elif (i == 2):
        q = c*np.array([rot[0][2]-rot[2][0], rot[1][0]+rot[0][1], A, rot[2][1]+rot[1][2]])
    else:
        q = c*np.array([rot[1][0]-rot[0][1], rot[0][2]+rot[2][0], rot[2][1]+rot[1][2], A])
    return q
