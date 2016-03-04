import behave
import nose.tools
from appli_poids import *

@given('height and gender and the ideal weight')
def step_impl(context):
    context.cp = CalculPoids()

@then('with 1.90 meter and man I obtain a ideal weight 80.0 kg')
def step_impl(context):
	nose.tools.assert_equal(context.cp.calcul_poids(1.90,0),80.0)

@then('with 1.60 meter and man I obtain a ideal weight 57.5 kg')
def step_impl(context):
	nose.tools.assert_equal(context.cp.calcul_poids(1.60,0),57.5)

@then('with 1.50 meter and woman I obtain a ideal weight 50.0 kg')
def step_impl(context):
	nose.tools.assert_equal(context.cp.calcul_poids(1.50,1),50.0)

@then('with 2.0 meter and woman I obtain a ideal weight 80.0 kg')
def step_impl(context):
	nose.tools.assert_equal(context.cp.calcul_poids(2.0,1),80.0)