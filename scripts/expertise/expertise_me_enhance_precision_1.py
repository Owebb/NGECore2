import sys

def addExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')
	
	if not player:
		return
		
	if not player.getProfession() == 'medic_1a':
		return
		
	actor.addSkill('expertise_me_enhance_precision_1')

	return
	
def removeExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')
	
	if not player:
		return
		
	if not player.getProfession() == 'medic_1a':
		return
		
	actor.removeSkill('expertise_me_enhance_precision_1')
	
	removeAbilities(core, actor, player)

	return

# this checks what abilities the player gets by level, need to also call this on level-up
def addAbilities(core, actor, player):
	
	actor.addAbility('me_buff_precision_1')
	actor.addAbility('me_buff_precision_2')
	actor.addAbility('me_buff_precision_3')
	
	return
	
def removeAbilities(core, actor, player):
	
	actor.removeAbility('me_buff_precision_1')
	actor.removeAbility('me_buff_precision_2')
	actor.removeAbility('me_buff_precision_3')
	
	return