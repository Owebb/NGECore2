import sys

def setup(core, actor, buff):
	core.skillModService.addSkillMod(actor, 'constitution_modified', 250)
	return
	
def removeBuff(core, actor, buff):
	core.skillModService.deductSkillMod(actor, 'constitution_modified', 250)
	return
	