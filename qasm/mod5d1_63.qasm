// This file has been taken from https://github.com/iic-jku/ibm_qx_mapping
OPENQASM 2.0;
include "qelib1.inc";
qreg q[16];
creg c[16];
cx q[3],q[1];
cx q[2],q[0];
cx q[1],q[4];
cx q[0],q[4];
h q[4];
t q[1];
t q[0];
t q[4];
cx q[0],q[1];
cx q[4],q[0];
cx q[1],q[4];
tdg q[0];
cx q[1],q[0];
tdg q[1];
tdg q[0];
t q[4];
cx q[4],q[0];
cx q[1],q[4];
cx q[0],q[1];
h q[4];
cx q[3],q[1];
cx q[2],q[0];
