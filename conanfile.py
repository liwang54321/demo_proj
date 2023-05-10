from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class test_placeRecipe(ConanFile):
    name = "test_place"
    version = "0.1.0"
    package_type = "application"

    license = "GPL"
    author = "wang.li wang.li@nio.com"
    url = "www.liwang54321.com"
    description = "wang.li test place"
    topics = ("test")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # def layout(self):
    #     cmake_layout(self)

    def configure(self):
        self.options['rttr'].with_rtti = True

    def requirements(self):
        self.requires('spdlog/1.11.0')
        self.requires('asio/1.27.0')
        self.requires('imgui/cci.20230105+1.89.2.docking')
        self.requires('clipp/1.2.3')
        self.requires('rttr/0.9.6')
        self.requires('boost/1.81.0')

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    
