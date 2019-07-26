#include <Python.h>

static PyObject* loop(PyObject* self)
{
    int i =0;
    for(i=0;i<10;i++)
    {
        printf("The number is %d\n",i);
    }
    Py_RETURN_NONE;
}

static char loop_docs[] = "loop(): This function is going to create a printing loop for 10 times.\n";

static PyMethodDef loop_methods[] = {
    {"loop", (PyCFunction)loop, METH_NOARGS, loop_docs},
    {NULL}
};

static struct PyModuleDef loop_module_def = 
{
    PyModuleDef_HEAD_INIT,
    "loop",
    "Module that is still in development",
    -1,
    loop_methods
};

PyMODINIT_FUNC PyInit_loop(void){
    Py_Initialize();

    return PyModule_Create(&loop_module_def);
}