import sys

def addExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')
	
	if not player:
		return
		
	if not player.getProfession() == 'medic_1a':
		return
		
	actor.addSkill('expertise_me_energy_armor_2')
	
	actor.addSkillMod('energy', 150)
	actor.addSkillMod('kinetic', 75)
	actor.addSkillMod('acid', 75)
	actor.addSkillMod('heat', 75)
	actor.addSkillMod('cold', 75)
	actor.addSkillMod('electricity', 75)
	
	addAbilities(core, actor, player)

	return
	
def removeExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')
	
	if not player:
		return
		
	if not player.getProfession() == 'medic_1a':
		return
		
	actor.removeSkill('expertise_me_energy_armor_2')
		
	actor.removeSkillMod('energy', 150)
	actor.removeSkillMod('kinetic', 75)
	actor.removeSkillMod('acid', 75)
	actor.removeSkillMod('heat', 75)
	actor.removeSkillMod('cold', 75)
	actor.removeSkillMod('electricity', 75)
	
	removeAbilities(core, actor, player)

	return

# this checks what abilities the player gets by level, need to also call this on level-up
def addAbilities(core, actor, player):

	return
	
def removeAbilities(core, actor, player):

	return