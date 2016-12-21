import unittest
import electropy as ep
import numpy as np

class ParticleTest(unittest.TestCase):

    def setUp(self):
        self.positionList = [-1, 2.5, 0]

    def tearDown(self):
        pass

    # Error/Exception Raise tests
    def test_that_particle_initialization_fails_for__non_list_or_np_array(self):
        positionVal = 0
        self.assertRaises(TypeError, ep.Particle, positionVal)

    def test_that_1D_list_position_throws_error_for_particle_initialization(self):
        position1D = [0]
        self.assertRaises(TypeError, ep.Particle, position1D)

    def test_that_1D_numpy_position_throws_error_for_particle_initialization(self):
        position1D = np.array([0])
        self.assertRaises(TypeError, ep.Particle, position1D)

    # Valid object initiation tests
    def test_that_3D_position_list_returns_an_object_of_type_Particle(self):
        assert(isinstance(ep.Particle(self.positionList), ep.Particle))

    def test_that_3D_numpy_array_returns_an_object_of_type_Particle(self):
        assert(isinstance(ep.Particle(np.array(self.positionList)), ep.Particle))

    #  Object property initialization tests
    def test_that_nparr_pos_attribute_is_not_equal_to_list_after_object_creation_using_list(self):
        testObj = ep.Particle(self.positionList)
        assert(~isinstance(testObj.pos, list))

    def test_that_list_pos_input_matches_the_nparr_pos_attribute_after_object_creation(self):
        testObj = ep.Particle(self.positionList)
        np.testing.assert_allclose(testObj.pos, np.array(self.positionList))

    def test_that_nparray_pos_input_matches_the_nparr_pos_attribute_after_object_creation(self):
        testObj = ep.Particle(np.array(self.positionList))
        np.testing.assert_allclose(testObj.pos, np.array(self.positionList))

    #  Decorators
    def test_that_x_decorator_gives_the_correct_pos_value(self):
        testObj = ep.Particle(self.positionList)
        self.assertEqual(testObj.x, self.positionList[0])

    def test_that_y_decorator_gives_the_correct_pos_value(self):
        testObj = ep.Particle(self.positionList)
        self.assertEqual(testObj.y, self.positionList[1])

    def test_that_z_decorator_gives_the_correct_pos_value(self):
        testObj = ep.Particle(self.positionList)
        self.assertEqual(testObj.z, self.positionList[2])
