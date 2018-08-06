from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")


name = "pybuilder-test-fail"
default_task = "publish"


@init
def set_properties(project):
    project.set_property("dir_source_main_python", "somecomponent")
    project.set_property("dir_source_unittest_python", "tests")
    project.set_property("unittest_module_glob", "test_*")
    project.set_property("unittest_test_method_prefix", "test_")
    project.set_property("dir_source_main_scripts", "scripts")
