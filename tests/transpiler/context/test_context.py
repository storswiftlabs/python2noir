import unittest
from transpiler.context.noir_context import NoirContext
from transpiler.core_module.statement_pod import Let
from transpiler.core_module.for_loop_pod import ForLoop
from transpiler.core_module.control_pod import IfControl
from transpiler.sub_module.primitive_type import UINT32, custom_type, INT64
from transpiler.sub_module.sign import LESS_THAN
from transpiler.utils.utils import table_format_control


class test_context(unittest.TestCase):
    def test_add_struct(self):
        struct_name = "Axis"
        name_and_type = {'node_name': 'u8', 'right': 'bool', 'left': 'bool'}
        context = NoirContext()
        context.add_struct(struct_name, name_and_type)
        struct_str = ""
        for line in context.generate_struct():
            struct_str += line
        print(struct_str)
        self.assertTrue(struct_str, """struct Axis { 
    node_name: u8;
    right: bool;
    left: bool;
    }""")

    def test_generate_noir(self):
        context = NoirContext()
        array_type = '[i64;6]'
        variate = 'sum'

        # Import Standard library
        # context.add_use()

        # add obtainEuclideanDistance function
        fn_name = 'obtainEuclideanDistance'
        fn_inputs_name_and_type = {'inputs': array_type, 'point': array_type}
        fn_result = INT64
        body = []

        let = Let(variate, INT64, 0, True).get()
        body.append(let)

        for_loop = ForLoop('index', 0, 5, 'sum += (point[index] - inputs[index]) *  (point[index] - inputs[index])') \
            .get()
        body.append(for_loop)

        body.append(variate)

        context.add_function(fn_name, fn_inputs_name_and_type, fn_result, body)

        # add check_min function
        fn_name = 'check_min'
        fn_inputs_name_and_type = {'e0': INT64, 'e1': INT64, 'e2': INT64, 'e3': INT64}
        fn_result = custom_type('u3')
        body = []

        let_output = Let('output', fn_result, 0, True).get()
        body.append(let_output)
        let_temp = Let('temp', INT64, 'e0', True).get()
        body.append(let_temp)

        sign = LESS_THAN
        control_1 = IfControl('e1', 'temp', sign, "temp = e1;\noutput = 1").get()
        body.append(control_1)
        control_2 = IfControl('e2', 'temp', sign, "temp = e2;\noutput = 2").get()
        body.append(control_2)
        control_3 = IfControl('e3', 'temp', sign, "temp = e3;\noutput = 3").get()
        body.append(control_3)

        body.append('output')

        context.add_function(fn_name, fn_inputs_name_and_type, fn_result, body)

        context.add_function_generics(
            fn_name, fn_inputs_name_and_type, fn_result, body, generics_type=True, generics_num=True)

        # add main function
        fn_name = 'main'
        fn_inputs_name_and_type = {'inputs': array_type, 'point0': array_type, 'point1': array_type,
                                   'point2': array_type, 'point3': array_type}
        fn_result = custom_type('u3')
        body = []

        let_e0 = Let('e0', INT64, 'obtainEuclideanDistance(inputs, point0)', False).get()
        body.append(let_e0)
        let_e1 = Let('e1', INT64, 'obtainEuclideanDistance(inputs, point1)', False).get()
        body.append(let_e1)
        let_e2 = Let('e2', INT64, 'obtainEuclideanDistance(inputs, point2)', False).get()
        body.append(let_e2)
        let_e3 = Let('e3', INT64, 'obtainEuclideanDistance(inputs, point3)', False).get()
        body.append(let_e3)

        body.append('check_min(e0,e1,e2,e3)')

        context.add_function(fn_name, fn_inputs_name_and_type, fn_result, body)


        noir_code = context.generate_noir_code_list()
        print(''.join(table_format_control(noir_code)))
        assert ''.join(table_format_control(noir_code)) == """// Code generated from Python2Noir
fn obtainEuclideanDistance(inputs : [i64;6],point : [i64;6],) -> pub i64 {
	let mut sum: i64 = 0;
	for index in 0..5 { 
		sum += (point[index] - inputs[index]) *  (point[index] - inputs[index])
	}
	sum
}
fn check_min(e0 : i64,e1 : i64,e2 : i64,e3 : i64,) -> pub u3 {
	let mut output: u3 = 0;
	let mut temp: i64 = e0;
	if e1 < temp { 
		temp = e1;
		output = 1
	}
	if e2 < temp { 
		temp = e2;
		output = 2
	}
	if e3 < temp { 
		temp = e3;
		output = 3
	}
	output
}
fn check_min<T, N>(e0 : i64,e1 : i64,e2 : i64,e3 : i64,) -> pub u3 {
	let mut output: u3 = 0;
	let mut temp: i64 = e0;
	if e1 < temp { 
		temp = e1;
		output = 1
	}
	if e2 < temp { 
		temp = e2;
		output = 2
	}
	if e3 < temp { 
		temp = e3;
		output = 3
	}
	output
}
fn main(inputs : [i64;6],point0 : [i64;6],point1 : [i64;6],point2 : [i64;6],point3 : [i64;6],) -> pub u3 {
	let e0: i64 = obtainEuclideanDistance(inputs, point0);
	let e1: i64 = obtainEuclideanDistance(inputs, point1);
	let e2: i64 = obtainEuclideanDistance(inputs, point2);
	let e3: i64 = obtainEuclideanDistance(inputs, point3);
	check_min(e0,e1,e2,e3)
}

"""

    def test_add_annotation(self):
        context = NoirContext()
        context.add_annotation(0, "will insert to line 0")
        context.add_annotation(2, "will insert to line 2")

        struct_name = "Axis"
        name_and_type = {'node_name': 'u8', 'right': 'bool', 'left': 'bool'}
        context.add_struct(struct_name, name_and_type)
        my_code = context.generate_struct()
        my_code = "".join(context.append_annotation(my_code))
        print(my_code)
        self.assertTrue(my_code, """// will insert to line 0
struct Axis { 
node_name: u8,
right: bool,
left: bool,
}
// will insert to line 2
""")


if __name__ == '__main__':
    unittest.main()
