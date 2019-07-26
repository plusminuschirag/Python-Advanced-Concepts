#include <Python.h>
#include <string.h>
#include <ctype.h>

static PyObject* counter(PyObject* self, PyObject* args)
{
    char *String = "";
    if (! PyArg_ParseTuple(args, "s", &String)) 
    { 
        return NULL; 
    }
    printf("%s\n",String);
    int size = strlen(String);
    return Py_BuildValue("i",size);
}

static PyObject* lowerCase(PyObject* self,PyObject* args)
{
    char *String = "";
    if (!PyArg_ParseTuple(args,"s",&String))
    {
        return NULL;
    }
    printf("Original String is : %s\n",String);
    for ( ; *String; ++String) *String = tolower(*String);
    return Py_BuildValue("s",String);
}

static char counter_docs[] = "counter(): Returns the length of string passed.\n";
static char lowerCase_docs[] = "lowercase(): Converts a string into lower case";
 
static PyMethodDef function_methods[] = {
    {"counter", (PyCFunction)counter, METH_VARARGS, counter_docs},
    {"divide", (PyCFunction)lowerCase, METH_VARARGS, lowerCase_docs},
    {NULL,NULL,0,NULL}
};


static struct PyModuleDef counter_lowercase_module_def = 
{
    PyModuleDef_HEAD_INIT,
    "counter",
    "Module that is still in development",
    -1,
    function_methods
};

PyMODINIT_FUNC PyInit_counter(void){
    Py_Initialize();

    return PyModule_Create(&counter_lowercase_module_def);
}