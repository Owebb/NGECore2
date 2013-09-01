import sys

def addExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')
	
	if not player:
		return
		
	if not player.getProfession() == 'medic_1a':
		return
		
	actor.addSkill('expertise_me_humanoid_crits_3')
	
	actor.addSkillMod('expertise_critical_niche_npc', 3)
	actor.addSkillMod('expertise_critical_niche_pvp', 3)
	
	addAbilities(core, actor, player)

	return
	
def removeExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')
	
	if not player:
		return
		
	if not player.getProfession() == 'medic_1a':
		return
		
	actor.removeSkill('expertise_me_humanoid_crits_3')
		
	actor.removeSkillMod('expertise_critical_niche_npc', 3)
	actor.removeSkillMod('expertise_critical_niche_pvp', 3)
	
	removeAbilities(core, actor, player)

	return

# this checks what abilities the player gets by level, need to also call this on level-up
def addAbilities(core, actor, player):

	return
	
def removeAbilities(core, actor, player):

	return