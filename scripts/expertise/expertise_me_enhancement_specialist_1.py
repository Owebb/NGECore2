import sys

def addExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')
	
	if not player:
		return
		
	if not player.getProfession() == 'medic_1a':
		return
		
	actor.addSkill('expertise_me_enhancement_specialist_1')

	return
	
def removeExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')
	
	if not player:
		return
		
	if not player.getProfession() == 'medic_1a':
		return
		
	actor.removeSkill('expertise_me_enhancement_specialist_1')
	
	removeAbilities(core, actor, player)

	return

# this checks what abilities the player gets by level, need to also call this on level-up
def addAbilities(core, actor, player):
	
	actor.addAbility('me_buff_action_1')
	actor.addAbility('me_buff_action_1')
	actor.addAbility('me_buff_action_1')
	actor.addAbility('me_buff_health')
	actor.addAbility('me_buff_action_0')
	actor.addAbility('me_buff_action_2')
	
	return
	
def removeAbilities(core, actor, player):
	
	actor.removeAbility('me_buff_action_1')
	actor.removeAbility('me_buff_action_1')
	actor.removeAbility('me_buff_action_1')
	actor.removeAbility('me_buff_health')
	actor.removeAbility('me_buff_health_0')
	actor.removeAbility('me_buff_health_0')
	
	return