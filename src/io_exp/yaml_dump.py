"""
This script allows for correct YAML formatting in regard to indentations.
See issue:
https://github.com/yaml/pyyaml/issues/234
See original idea:
https://stackoverflow.com/questions/25108581/python-yaml-dump-bad-indentation

"""
import os
import yaml

__CURR_DIR = os.path.dirname(__file__)

class MyDumper(yaml.Dumper):

    # def increase_indent(self, flow=False, indentless=False):
    #     return super(MyDumper, self).increase_indent(flow, False)

    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)
foo = {
    'name': 'foo',
    'my_list': [
        {'foo': 'test', 'bar': 'test2'},
        {'foo': 'test3', 'bar': 'test4'}],
    'hello': 'world',
}

print(yaml.dump(foo, Dumper=MyDumper, default_flow_style=False))
import os
with open(os.path.join(__CURR_DIR, 'foo.yaml'), 'w') as f:
    yaml.dump(foo, f, Dumper=MyDumper, default_flow_style=False, explicit_start=True,
              sort_keys=False,
              allow_unicode=True,
              indent=2,
              line_break=os.linesep,
              # canonical=True,
              )

"""
Output with canonical=False:
---
name: foo
my_list:
  - foo: test
    bar: test2
  - foo: test3
    bar: test4
hello: world


Output with canonical=True:
---
!!map {
  ? !!str "name"
  : !!str "foo",
  ? !!str "my_list"
  : !!seq [
    !!map {
      ? !!str "foo"
      : !!str "test",
      ? !!str "bar"
      : !!str "test2",
    },
    !!map {
      ? !!str "foo"
      : !!str "test3",
      ? !!str "bar"
      : !!str "test4",
    },
  ],
  ? !!str "hello"
  : !!str "world",
}
"""
