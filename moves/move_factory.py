from moves.bug_moves.attack_order import AttackOrder
from moves.bug_moves.bug_bite import BugBite
from moves.bug_moves.first_impression import FirstImpression
from moves.bug_moves.fury_cutter import FuryCutter
from moves.bug_moves.heal_order import HealOrder
from moves.bug_moves.infestation import Infestation
from moves.bug_moves.leech_life import LeechLife
from moves.bug_moves.megahorn import Megahorn
from moves.bug_moves.pin_missile import PinMissile
from moves.bug_moves.pollen_puff import PollenPuff
from moves.bug_moves.powder import Powder
from moves.bug_moves.rage_powder import RagePowder
from moves.bug_moves.savage_spin_out import SavageSpinOut
from moves.bug_moves.signal_beam import SignalBeam
from moves.bug_moves.silver_wind import SilverWind
from moves.bug_moves.spider_web import SpiderWeb
from moves.bug_moves.tail_glow import TailGlow
from moves.bug_moves.u_turn import Uturn
from moves.bug_moves.x_scissor import XScissor
from moves.dark_moves.assurance import Assurance
from moves.dark_moves.baddy_bad import BaddyBad
from moves.dark_moves.beat_up import BeatUp
from moves.dark_moves.black_hole_eclipse import BlackHoleEclipse
from moves.dark_moves.brutal_swing import BrutalSwing
from moves.dark_moves.ceaseless_edge import CeaselessEdge
from moves.dark_moves.comeuppance import Comeuppance
from moves.dark_moves.crunch import Crunch
from moves.dark_moves.darkest_lariat import DarkestLariat
from moves.dark_moves.dark_void import DarkVoid
from moves.dark_moves.embargo import Embargo
from moves.dark_moves.false_surrender import FalseSurrender
from moves.dark_moves.feint_attack import FeintAttack
from moves.dark_moves.fling import Fling
from moves.dark_moves.foul_play import FoulPlay
from moves.dark_moves.jaw_lock import JawLock
from moves.dark_moves.knock_off import KnockOff
from moves.dark_moves.kowtow_cleave import KowtowCleave
from moves.dark_moves.lash_out import LashOut
from moves.dark_moves.malicious_moonsault import MaliciousMoonsault
from moves.dark_moves.night_daze import NightDaze
from moves.dark_moves.night_slash import NightSlash
from moves.dark_moves.payback import Payback
from moves.dark_moves.power_trip import PowerTrip
from moves.dark_moves.punishment import Punishment
from moves.dark_moves.pursuit import Pursuit
from moves.dark_moves.quash import Quash
from moves.dark_moves.ruination import Ruination
from moves.dark_moves.snatch import Snatch
from moves.dark_moves.sucker_punch import SuckerPunch
from moves.dark_moves.switcheroo import Switcheroo
from moves.dark_moves.thief import Thief
from moves.dark_moves.throat_chop import ThroatChop
from moves.dark_moves.torment import Torment
from moves.dark_moves.wicked_blow import WickedBlow
from moves.dark_moves.wicked_torque import WickedTorque
from moves.dragon_moves.clangorous_soulblaze import ClangorousSoulblaze
from moves.dragon_moves.core_enforcer import CoreEnforcer
from moves.dragon_moves.devastating_drake import DevastatingDrake
from moves.dragon_moves.dragon_claw import DragonClaw
from moves.dragon_moves.dragon_darts import DragonDarts
from moves.dragon_moves.dragon_energy import DragonEnergy
from moves.dragon_moves.dragon_hammer import DragonHammer
from moves.dragon_moves.dragon_pulse import DragonPulse
from moves.dragon_moves.dragon_rage import DragonRage
from moves.dragon_moves.dragon_tail import DragonTail
from moves.dragon_moves.dual_chop import DualChop
from moves.dragon_moves.dynamax_cannon import DynamaxCannon
from moves.dragon_moves.eternabeam import Eternabeam
from moves.dragon_moves.glaive_rush import GlaiveRush
from moves.dragon_moves.order_up import OrderUp
from moves.dragon_moves.roar_of_time import RoarofTime
from moves.dragon_moves.spacial_rend import SpacialRend
from moves.electric_moves.aura_wheel import AuraWheel
from moves.electric_moves.bolt_beak import BoltBeak
from moves.electric_moves.buzzy_buzz import BuzzyBuzz
from moves.electric_moves.catastropika import Catastropika
from moves.electric_moves.charge_beam import ChargeBeam
from moves.electric_moves.double_shock import DoubleShock
from moves.electric_moves.electrify import Electrify
from moves.electric_moves.electro_ball import ElectroBall
from moves.electric_moves.electro_drift import ElectroDrift
from moves.electric_moves.fusion_bolt import FusionBolt
from moves.electric_moves.gigavolt_havoc import GigavoltHavoc
from moves.electric_moves.ion_deluge import IonDeluge
from moves.electric_moves.magnet_rise import MagnetRise
from moves.electric_moves.nuzzle import Nuzzle
from moves.electric_moves.overdrive import Overdrive
from moves.electric_moves.parabolic_charge import ParabolicCharge
from moves.electric_moves.pika_papow import PikaPapow
from moves.electric_moves.plasma_fists import PlasmaFists
from moves.electric_moves.rising_voltage import RisingVoltage
from moves.electric_moves.shock_wave import ShockWave
from moves.electric_moves.stoked_sparksurfer import StokedSparksurfer
from moves.electric_moves.thunder_cage import ThunderCage
from moves.electric_moves.thunder_wave import ThunderWave
from moves.electric_moves.volt_switch import VoltSwitch
from moves.electric_moves.wildbolt_storm import WildboltStorm
from moves.electric_moves.wild_charge import WildCharge
from moves.electric_moves.zap_cannon import ZapCannon
from moves.electric_moves.zippy_zap import ZippyZap
from moves.fairy_moves.crafty_shield import CraftyShield
from moves.fairy_moves.dazzling_gleam import DazzlingGleam
from moves.fairy_moves.disarming_voice import DisarmingVoice
from moves.fairy_moves.draining_kiss import DrainingKiss
from moves.fairy_moves.fairy_lock import FairyLock
from moves.fairy_moves.fairy_wind import FairyWind
from moves.fairy_moves.floral_healing import FloralHealing
from moves.fairy_moves.guardian_of_alola import GuardianofAlola
from moves.fairy_moves.light_of_ruin import LightofRuin
from moves.fairy_moves.magical_torque import MagicalTorque
from moves.fairy_moves.misty_explosion import MistyExplosion
from moves.fairy_moves.misty_terrain import MistyTerrain
from moves.fairy_moves.moonblast import Moonblast
from moves.fairy_moves.moonlight import Moonlight
from moves.fairy_moves.nature_madness import NatureMadness
from moves.fairy_moves.play_rough import PlayRough
from moves.fairy_moves.sparkly_swirl import SparklySwirl
from moves.fairy_moves.strange_steam import StrangeSteam
from moves.fairy_moves.sweet_kiss import SweetKiss
from moves.fairy_moves.twinkle_tackle import TwinkleTackle
from moves.fighting_moves.arm_thrust import ArmThrust
from moves.fighting_moves.aura_sphere import AuraSphere
from moves.fighting_moves.axe_kick import AxeKick
from moves.fighting_moves.body_press import BodyPress
from moves.fighting_moves.brick_break import BrickBreak
from moves.fighting_moves.circle_throw import CircleThrow
from moves.fighting_moves.coaching import Coaching
from moves.fighting_moves.collision_course import CollisionCourse
from moves.fighting_moves.combat_torque import CombatTorque
from moves.fighting_moves.counter import Counter
from moves.fighting_moves.cross_chop import CrossChop
from moves.fighting_moves.detect import Detect
from moves.fighting_moves.double_kick import DoubleKick
from moves.fighting_moves.drain_punch import DrainPunch
from moves.fighting_moves.dynamic_punch import DynamicPunch
from moves.fighting_moves.final_gambit import FinalGambit
from moves.fighting_moves.flying_press import FlyingPress
from moves.fighting_moves.focus_blast import FocusBlast
from moves.fighting_moves.focus_punch import FocusPunch
from moves.fighting_moves.high_jump_kick import HighJumpKick
from moves.fighting_moves.jump_kick import JumpKick
from moves.fighting_moves.karate_chop import KarateChop
from moves.fighting_moves.low_kick import LowKick
from moves.fighting_moves.mach_punch import MachPunch
from moves.fighting_moves.mat_block import MatBlock
from moves.fighting_moves.meteor_assault import MeteorAssault
from moves.fighting_moves.quick_guard import QuickGuard
from moves.fighting_moves.revenge import Revenge
from moves.fighting_moves.reversal import Reversal
from moves.fighting_moves.rock_smash import RockSmash
from moves.fighting_moves.sacred_sword import SacredSword
from moves.fighting_moves.secret_sword import SecretSword
from moves.fighting_moves.seismic_toss import SeismicToss
from moves.fighting_moves.sky_uppercut import SkyUppercut
from moves.fighting_moves.storm_throw import StormThrow
from moves.fighting_moves.submission import Submission
from moves.fighting_moves.thunderous_kick import ThunderousKick
from moves.fighting_moves.triple_arrows import TripleArrows
from moves.fighting_moves.triple_kick import TripleKick
from moves.fighting_moves.vacuum_wave import VacuumWave
from moves.fighting_moves.victory_dance import VictoryDance
from moves.fighting_moves.vital_throw import VitalThrow
from moves.fighting_moves.wake_up_slap import WakeUpSlap
from moves.fire_moves.bitter_blade import BitterBlade
from moves.fire_moves.blast_burn import BlastBurn
from moves.fire_moves.blazing_torque import BlazingTorque
from moves.fire_moves.burning_jealousy import BurningJealousy
from moves.fire_moves.burn_up import BurnUp
from moves.fire_moves.eruption import Eruption
from moves.fire_moves.fiery_dance import FieryDance
from moves.fire_moves.fire_pledge import FirePledge
from moves.fire_moves.fire_spin import FireSpin
from moves.fire_moves.flame_burst import FlameBurst
from moves.fire_moves.fusion_flare import FusionFlare
from moves.fire_moves.heat_crash import HeatCrash
from moves.fire_moves.incinerate import Incinerate
from moves.fire_moves.inferno import Inferno
from moves.fire_moves.inferno_overdrive import InfernoOverdrive
from moves.fire_moves.magma_storm import MagmaStorm
from moves.fire_moves.mind_blown import MindBlown
from moves.fire_moves.raging_fury import RagingFury
from moves.fire_moves.shell_trap import ShellTrap
from moves.fire_moves.sizzly_slide import SizzlySlide
from moves.fire_moves.sunny_day import SunnyDay
from moves.fire_moves.torch_song import TorchSong
from moves.flying_moves.acrobatics import Acrobatics
from moves.flying_moves.aerial_ace import AerialAce
from moves.flying_moves.aeroblast import Aeroblast
from moves.flying_moves.air_cutter import AirCutter
from moves.flying_moves.beak_blast import BeakBlast
from moves.flying_moves.bleakwind_storm import BleakwindStorm
from moves.flying_moves.brave_bird import BraveBird
from moves.flying_moves.chatter import Chatter
from moves.flying_moves.drill_peck import DrillPeck
from moves.flying_moves.dual_wingbeat import DualWingbeat
from moves.flying_moves.fly import Fly
from moves.flying_moves.gust import Gust
from moves.flying_moves.hurricane import Hurricane
from moves.flying_moves.mirror_move import MirrorMove
from moves.flying_moves.oblivion_wing import OblivionWing
from moves.flying_moves.peck import Peck
from moves.flying_moves.pluck import Pluck
from moves.flying_moves.roost import Roost
from moves.flying_moves.sky_drop import SkyDrop
from moves.flying_moves.supersonic_skystrike import SupersonicSkystrike
from moves.flying_moves.tailwind import Tailwind
from moves.flying_moves.wing_attack import WingAttack
from moves.ghost_moves.astral_barrage import AstralBarrage
from moves.ghost_moves.bitter_malice import BitterMalice
from moves.ghost_moves.confuse_ray import ConfuseRay
from moves.ghost_moves.curse import Curse
from moves.ghost_moves.destiny_bond import DestinyBond
from moves.ghost_moves.grudge import Grudge
from moves.ghost_moves.hex import Hex
from moves.ghost_moves.infernal_parade import InfernalParade
from moves.ghost_moves.last_respects import LastRespects
from moves.ghost_moves.menacing_moonraze_maelstrom import MenacingMoonrazeMaelstrom
from moves.ghost_moves.moongeist_beam import MoongeistBeam
from moves.ghost_moves.nightmare import Nightmare
from moves.ghost_moves.night_shade import NightShade
from moves.ghost_moves.ominous_wind import OminousWind
from moves.ghost_moves.phantom_force import PhantomForce
from moves.ghost_moves.rage_fist import RageFist
from moves.ghost_moves.shadow_ball import ShadowBall
from moves.ghost_moves.shadow_bone import ShadowBone
from moves.ghost_moves.shadow_claw import ShadowClaw
from moves.ghost_moves.shadow_force import ShadowForce
from moves.ghost_moves.shadow_punch import ShadowPunch
from moves.ghost_moves.shadow_sneak import ShadowSneak
from moves.ghost_moves.sinister_arrow_raid import SinisterArrowRaid
from moves.ghost_moves.spectral_thief import SpectralThief
from moves.ghost_moves.spirit_shackle import SpiritShackle
from moves.ghost_moves.spite import Spite
from moves.ghost_moves.trick_or_treat import TrickorTreat
from moves.grass_moves.absorb import Absorb
from moves.grass_moves.aromatherapy import Aromatherapy
from moves.grass_moves.bloom_doom import BloomDoom
from moves.grass_moves.branch_poke import BranchPoke
from moves.grass_moves.bullet_seed import BulletSeed
from moves.grass_moves.chloroblast import Chloroblast
from moves.grass_moves.energy_ball import EnergyBall
from moves.grass_moves.flower_trick import FlowerTrick
from moves.grass_moves.forest_curse import ForestCurse
from moves.grass_moves.frenzy_plant import FrenzyPlant
from moves.grass_moves.giga_drain import GigaDrain
from moves.grass_moves.grassy_glide import GrassyGlide
from moves.grass_moves.grassy_terrain import GrassyTerrain
from moves.grass_moves.grass_knot import GrassKnot
from moves.grass_moves.grass_pledge import GrassPledge
from moves.grass_moves.horn_leech import HornLeech
from moves.grass_moves.ingrain import Ingrain
from moves.grass_moves.jungle_healing import JungleHealing
from moves.grass_moves.leafage import Leafage
from moves.grass_moves.leaf_blade import LeafBlade
from moves.grass_moves.leaf_tornado import LeafTornado
from moves.grass_moves.leech_seed import LeechSeed
from moves.grass_moves.magical_leaf import MagicalLeaf
from moves.grass_moves.mega_drain import MegaDrain
from moves.grass_moves.petal_blizzard import PetalBlizzard
from moves.grass_moves.power_whip import PowerWhip
from moves.grass_moves.razor_leaf import RazorLeaf
from moves.grass_moves.sappy_seed import SappySeed
from moves.grass_moves.seed_bomb import SeedBomb
from moves.grass_moves.seed_flare import SeedFlare
from moves.grass_moves.snap_trap import SnapTrap
from moves.grass_moves.solar_beam import SolarBeam
from moves.grass_moves.solar_blade import SolarBlade
from moves.grass_moves.spiky_shield import SpikyShield
from moves.grass_moves.stun_spore import StunSpore
from moves.grass_moves.synthesis import Synthesis
from moves.grass_moves.trailblaze import Trailblaze
from moves.grass_moves.trop_kick import TropKick
from moves.grass_moves.vine_whip import VineWhip
from moves.grass_moves.wood_hammer import WoodHammer
from moves.grass_moves.worry_seed import WorrySeed
from moves.ground_moves.bonemerang import Bonemerang
from moves.ground_moves.bone_rush import BoneRush
from moves.ground_moves.dig import Dig
from moves.ground_moves.drill_run import DrillRun
from moves.ground_moves.earthquake import Earthquake
from moves.ground_moves.earth_power import EarthPower
from moves.ground_moves.fissure import Fissure
from moves.ground_moves.high_horsepower import HighHorsepower
from moves.ground_moves.land_wrath import LandWrath
from moves.ground_moves.magnitude import Magnitude
from moves.ground_moves.mud_bomb import MudBomb
from moves.ground_moves.mud_sport import MudSport
from moves.ground_moves.precipice_blades import PrecipiceBlades
from moves.ground_moves.sandsear_storm import SandsearStorm
from moves.ground_moves.sand_tomb import SandTomb
from moves.ground_moves.scorching_sands import ScorchingSands
from moves.ground_moves.shore_up import ShoreUp
from moves.ground_moves.spikes import Spikes
from moves.ground_moves.stomping_tantrum import StompingTantrum
from moves.ground_moves.tectonic_rage import TectonicRage
from moves.ground_moves.thousand_arrows import ThousandArrows
from moves.ground_moves.thousand_waves import ThousandWaves
from moves.ice_moves.aurora_beam import AuroraBeam
from moves.ice_moves.aurora_veil import AuroraVeil
from moves.ice_moves.avalanche import Avalanche
from moves.ice_moves.chilly_reception import ChillyReception
from moves.ice_moves.freezy_frost import FreezyFrost
from moves.ice_moves.frost_breath import FrostBreath
from moves.ice_moves.glacial_lance import GlacialLance
from moves.ice_moves.hail import Hail
from moves.ice_moves.haze import Haze
from moves.ice_moves.ice_ball import IceBall
from moves.ice_moves.ice_shard import IceShard
from moves.ice_moves.ice_spinner import IceSpinner
from moves.ice_moves.icicle_spear import IcicleSpear
from moves.ice_moves.mist import Mist
from moves.ice_moves.sheer_cold import SheerCold
from moves.ice_moves.subzero_slammer import SubzeroSlammer
from moves.ice_moves.triple_axel import TripleAxel
from moves.normal_moves.after_you import AfterYou
from moves.normal_moves.assist import Assist
from moves.normal_moves.attract import Attract
from moves.normal_moves.barrage import Barrage
from moves.normal_moves.baton_pass import BatonPass
from moves.normal_moves.bestow import Bestow
from moves.normal_moves.bide import Bide
from moves.normal_moves.bind import Bind
from moves.normal_moves.block import Block
from moves.normal_moves.boomburst import Boomburst
from moves.normal_moves.breakneck_blitz import BreakneckBlitz
from moves.normal_moves.camouflage import Camouflage
from moves.normal_moves.celebrate import Celebrate
from moves.normal_moves.chip_away import ChipAway
from moves.normal_moves.comet_punch import CometPunch
from moves.normal_moves.constrict import Constrict
from moves.normal_moves.conversion import Conversion
from moves.normal_moves.conversion_2 import Conversion2
from moves.normal_moves.copycat import Copycat
from moves.normal_moves.court_change import CourtChange
from moves.normal_moves.covet import Covet
from moves.normal_moves.crush_claw import CrushClaw
from moves.normal_moves.crush_grip import CrushGrip
from moves.normal_moves.cut import Cut
from moves.normal_moves.disable import Disable
from moves.normal_moves.dizzy_punch import DizzyPunch
from moves.normal_moves.doodle import Doodle
from moves.normal_moves.double_edge import DoubleEdge
from moves.normal_moves.double_hit import DoubleHit
from moves.normal_moves.double_slap import DoubleSlap
from moves.normal_moves.echoed_voice import EchoedVoice
from moves.normal_moves.egg_bomb import EggBomb
from moves.normal_moves.encore import Encore
from moves.normal_moves.endeavor import Endeavor
from moves.normal_moves.endure import Endure
from moves.normal_moves.entrainment import Entrainment
from moves.normal_moves.explosion import Explosion
from moves.normal_moves.extreme_speed import ExtremeSpeed
from moves.normal_moves.facade import Facade
from moves.normal_moves.fake_out import FakeOut
from moves.normal_moves.false_swipe import FalseSwipe
from moves.normal_moves.feint import Feint
from moves.normal_moves.flail import Flail
from moves.normal_moves.focus_energy import FocusEnergy
from moves.normal_moves.follow_me import FollowMe
from moves.normal_moves.foresight import Foresight
from moves.normal_moves.frustration import Frustration
from moves.normal_moves.fury_attack import FuryAttack
from moves.normal_moves.fury_swipes import FurySwipes
from moves.normal_moves.giga_impact import GigaImpact
from moves.normal_moves.glare import Glare
from moves.normal_moves.guillotine import Guillotine
from moves.normal_moves.happy_hour import HappyHour
from moves.normal_moves.head_charge import HeadCharge
from moves.normal_moves.heal_bell import HealBell
from moves.normal_moves.helping_hand import HelpingHand
from moves.normal_moves.hidden_power import HiddenPower
from moves.normal_moves.hold_back import HoldBack
from moves.normal_moves.hold_hands import HoldHands
from moves.normal_moves.horn_attack import HornAttack
from moves.normal_moves.horn_drill import HornDrill
from moves.normal_moves.hyper_beam import HyperBeam
from moves.normal_moves.hyper_drill import HyperDrill
from moves.normal_moves.hyper_voice import HyperVoice
from moves.normal_moves.judgment import Judgment
from moves.normal_moves.laser_focus import LaserFocus
from moves.normal_moves.last_resort import LastResort
from moves.normal_moves.lock_on import LockOn
from moves.normal_moves.lucky_chant import LuckyChant
from moves.normal_moves.mean_look import MeanLook
from moves.normal_moves.mega_kick import MegaKick
from moves.normal_moves.mega_punch import MegaPunch
from moves.normal_moves.metronome import Metronome
from moves.normal_moves.me_first import MeFirst
from moves.normal_moves.milk_drink import MilkDrink
from moves.normal_moves.mimic import Mimic
from moves.normal_moves.mind_reader import MindReader
from moves.normal_moves.morning_sun import MorningSun
from moves.normal_moves.multi_attack import MultiAttack
from moves.normal_moves.natural_gift import NaturalGift
from moves.normal_moves.nature_power import NaturePower
from moves.normal_moves.odor_sleuth import OdorSleuth
from moves.normal_moves.pain_split import PainSplit
from moves.normal_moves.pay_day import PayDay
from moves.normal_moves.perish_song import PerishSong
from moves.normal_moves.population_bomb import PopulationBomb
from moves.normal_moves.pound import Pound
from moves.normal_moves.power_shift import PowerShift
from moves.normal_moves.present import Present
from moves.normal_moves.protect import Protect
from moves.normal_moves.psych_up import PsychUp
from moves.normal_moves.pulverizing_pancake import PulverizingPancake
from moves.normal_moves.quick_attack import QuickAttack
from moves.normal_moves.raging_bull import RagingBull
from moves.normal_moves.razor_wind import RazorWind
from moves.normal_moves.recover import Recover
from moves.normal_moves.recycle import Recycle
from moves.normal_moves.reflect_type import ReflectType
from moves.normal_moves.refresh import Refresh
from moves.normal_moves.relic_song import RelicSong
from moves.normal_moves.retaliate import Retaliate
from moves.normal_moves.return_ import Return
from moves.normal_moves.revelation_dance import RevelationDance
from moves.normal_moves.revival_blessing import RevivalBlessing
from moves.normal_moves.roar import Roar
from moves.normal_moves.rock_climb import RockClimb
from moves.normal_moves.round import Round
from moves.normal_moves.safeguard import Safeguard
from moves.normal_moves.scratch import Scratch
from moves.normal_moves.secret_power import SecretPower
from moves.normal_moves.self_destruct import SelfDestruct
from moves.normal_moves.shed_tail import ShedTail
from moves.normal_moves.simple_beam import SimpleBeam
from moves.normal_moves.sketch import Sketch
from moves.normal_moves.slack_off import SlackOff
from moves.normal_moves.slam import Slam
from moves.normal_moves.slash import Slash
from moves.normal_moves.sleep_talk import SleepTalk
from moves.normal_moves.smelling_salts import SmellingSalts
from moves.normal_moves.soft_boiled import SoftBoiled
from moves.normal_moves.sonic_boom import SonicBoom
from moves.normal_moves.spike_cannon import SpikeCannon
from moves.normal_moves.spit_up import SpitUp
from moves.normal_moves.splash import Splash
from moves.normal_moves.spotlight import Spotlight
from moves.normal_moves.stockpile import Stockpile
from moves.normal_moves.strength import Strength
from moves.normal_moves.struggle import Struggle
from moves.normal_moves.substitute import Substitute
from moves.normal_moves.supersonic import Supersonic
from moves.normal_moves.super_fang import SuperFang
from moves.normal_moves.swallow import Swallow
from moves.normal_moves.swift import Swift
from moves.normal_moves.tackle import Tackle
from moves.normal_moves.tail_slap import TailSlap
from moves.normal_moves.tail_whip import TailWhip
from moves.normal_moves.take_down import TakeDown
from moves.normal_moves.tearful_look import TearfulLook
from moves.normal_moves.teatime import Teatime
from moves.normal_moves.techno_blast import TechnoBlast
from moves.normal_moves.teeter_dance import TeeterDance
from moves.normal_moves.tera_blast import TeraBlast
from moves.normal_moves.terrain_pulse import TerrainPulse
from moves.normal_moves.tickle import Tickle
from moves.normal_moves.tidy_up import TidyUp
from moves.normal_moves.transform import Transform
from moves.normal_moves.trump_card import TrumpCard
from moves.normal_moves.uproar import Uproar
from moves.normal_moves.veevee_volley import VeeveeVolley
from moves.normal_moves.vise_grip import ViseGrip
from moves.normal_moves.weather_ball import WeatherBall
from moves.normal_moves.whirlwind import Whirlwind
from moves.normal_moves.wish import Wish
from moves.normal_moves.work_up import WorkUp
from moves.normal_moves.wrap import Wrap
from moves.normal_moves.wring_out import WringOut
from moves.poison_moves.acid import Acid
from moves.poison_moves.acid_downpour import AcidDownpour
from moves.poison_moves.baneful_bunker import BanefulBunker
from moves.poison_moves.barb_barrage import BarbBarrage
from moves.poison_moves.belch import Belch
from moves.poison_moves.clear_smog import ClearSmog
from moves.poison_moves.corrosive_gas import CorrosiveGas
from moves.poison_moves.dire_claw import DireClaw
from moves.poison_moves.gastro_acid import GastroAcid
from moves.poison_moves.mortal_spin import MortalSpin
from moves.poison_moves.noxious_torque import NoxiousTorque
from moves.poison_moves.poison_gas import PoisonGas
from moves.poison_moves.poison_jab import PoisonJab
from moves.poison_moves.poison_powder import PoisonPowder
from moves.poison_moves.poison_sting import PoisonSting
from moves.poison_moves.purify import Purify
from moves.poison_moves.toxic import Toxic
from moves.poison_moves.toxic_spikes import ToxicSpikes
from moves.poison_moves.toxic_thread import ToxicThread
from moves.poison_moves.venom_drench import VenomDrench
from moves.poison_moves.venoshock import Venoshock
from moves.psychic_moves.ally_switch import AllySwitch
from moves.psychic_moves.confusion import Confusion
from moves.psychic_moves.dream_eater import DreamEater
from moves.psychic_moves.eerie_spell import EerieSpell
from moves.psychic_moves.expanding_force import ExpandingForce
from moves.psychic_moves.future_sight import FutureSight
from moves.psychic_moves.genesis_supernova import GenesisSupernova
from moves.psychic_moves.glitzy_glow import GlitzyGlow
from moves.psychic_moves.gravity import Gravity
from moves.psychic_moves.guard_split import GuardSplit
from moves.psychic_moves.guard_swap import GuardSwap
from moves.psychic_moves.healing_wish import HealingWish
from moves.psychic_moves.heal_block import HealBlock
from moves.psychic_moves.heal_pulse import HealPulse
from moves.psychic_moves.heart_swap import HeartSwap
from moves.psychic_moves.hyperspace_hole import HyperspaceHole
from moves.psychic_moves.imprison import Imprison
from moves.psychic_moves.instruct import Instruct
from moves.psychic_moves.light_screen import LightScreen
from moves.psychic_moves.light_that_burns_the_sky import LightThatBurnstheSky
from moves.psychic_moves.lunar_blessing import LunarBlessing
from moves.psychic_moves.lunar_dance import LunarDance
from moves.psychic_moves.luster_purge import LusterPurge
from moves.psychic_moves.magic_coat import MagicCoat
from moves.psychic_moves.magic_powder import MagicPowder
from moves.psychic_moves.magic_room import MagicRoom
from moves.psychic_moves.miracle_eye import MiracleEye
from moves.psychic_moves.mirror_coat import MirrorCoat
from moves.psychic_moves.mist_ball import MistBall
from moves.psychic_moves.photon_geyser import PhotonGeyser
from moves.psychic_moves.power_split import PowerSplit
from moves.psychic_moves.power_swap import PowerSwap
from moves.psychic_moves.power_trick import PowerTrick
from moves.psychic_moves.prismatic_laser import PrismaticLaser
from moves.psychic_moves.psybeam import Psybeam
from moves.psychic_moves.psyblade import Psyblade
from moves.psychic_moves.psychic import Psychic
from moves.psychic_moves.psychic_fangs import PsychicFangs
from moves.psychic_moves.psychic_terrain import PsychicTerrain
from moves.psychic_moves.psycho_cut import PsychoCut
from moves.psychic_moves.psycho_shift import PsychoShift
from moves.psychic_moves.psyshock import Psyshock
from moves.psychic_moves.psystrike import Psystrike
from moves.psychic_moves.psywave import Psywave
from moves.psychic_moves.reflect import Reflect
from moves.psychic_moves.rest import Rest
from moves.psychic_moves.role_play import RolePlay
from moves.psychic_moves.shattered_psyche import ShatteredPsyche
from moves.psychic_moves.skill_swap import SkillSwap
from moves.psychic_moves.speed_swap import SpeedSwap
from moves.psychic_moves.stored_power import StoredPower
from moves.psychic_moves.synchronoise import Synchronoise
from moves.psychic_moves.take_heart import TakeHeart
from moves.psychic_moves.telekinesis import Telekinesis
from moves.psychic_moves.teleport import Teleport
from moves.psychic_moves.trick import Trick
from moves.psychic_moves.trick_room import TrickRoom
from moves.psychic_moves.twin_beam import TwinBeam
from moves.psychic_moves.wonder_room import WonderRoom
from moves.rock_moves.accelerock import Accelerock
from moves.rock_moves.ancient_power import AncientPower
from moves.rock_moves.continental_crush import ContinentalCrush
from moves.rock_moves.diamond_storm import DiamondStorm
from moves.rock_moves.head_smash import HeadSmash
from moves.rock_moves.meteor_beam import MeteorBeam
from moves.rock_moves.power_gem import PowerGem
from moves.rock_moves.rock_blast import RockBlast
from moves.rock_moves.rock_throw import RockThrow
from moves.rock_moves.rock_wrecker import RockWrecker
from moves.rock_moves.rollout import Rollout
from moves.rock_moves.salt_cure import SaltCure
from moves.rock_moves.sandstorm import Sandstorm
from moves.rock_moves.smack_down import SmackDown
from moves.rock_moves.splintered_stormshards import SplinteredStormshards
from moves.rock_moves.stealth_rock import StealthRock
from moves.rock_moves.stone_axe import StoneAxe
from moves.rock_moves.stone_edge import StoneEdge
from moves.rock_moves.tar_shot import TarShot
from moves.rock_moves.wide_guard import WideGuard
from moves.status_moves.bug_moves.steamroller import Steamroller
from moves.status_moves.bug_moves.twineedle import Twineedle
from moves.status_moves.dark_moves.bite import Bite
from moves.status_moves.dark_moves.dark_pulse import DarkPulse
from moves.status_moves.dark_moves.fiery_wrath import FieryWrath
from moves.status_moves.dark_moves.taunt import Taunt
from moves.status_moves.dragon_moves.dragon_breath import DragonBreath
from moves.status_moves.dragon_moves.dragon_rush import DragonRush
from moves.status_moves.dragon_moves.outrage import Outrage
from moves.status_moves.dragon_moves.twister import Twister
from moves.status_moves.electric_moves.bolt_strike import BoltStrike
from moves.status_moves.electric_moves.discharge import Discharge
from moves.status_moves.electric_moves.spark import Spark
from moves.status_moves.electric_moves.thunder import Thunder
from moves.status_moves.electric_moves.thunderbolt import Thunderbolt
from moves.status_moves.electric_moves.thunder_fang import ThunderFang
from moves.status_moves.electric_moves.thunder_punch import ThunderPunch
from moves.status_moves.electric_moves.thunder_shock import ThunderShock
from moves.status_moves.electric_moves.volt_tackle import VoltTackle
from moves.status_moves.electric_moves.zing_zap import ZingZap
from moves.status_moves.fighting_moves.force_palm import ForcePalm
from moves.status_moves.fighting_moves.rolling_kick import RollingKick
from moves.status_moves.fire_moves.blaze_kick import BlazeKick
from moves.status_moves.fire_moves.blue_flare import BlueFlare
from moves.status_moves.fire_moves.ember import Ember
from moves.status_moves.fire_moves.fire_blast import FireBlast
from moves.status_moves.fire_moves.fire_fang import FireFang
from moves.status_moves.fire_moves.fire_punch import FirePunch
from moves.status_moves.fire_moves.flamethrower import Flamethrower
from moves.status_moves.fire_moves.flame_wheel import FlameWheel
from moves.status_moves.fire_moves.flare_blitz import FlareBlitz
from moves.status_moves.fire_moves.heat_wave import HeatWave
from moves.status_moves.fire_moves.lava_plume import LavaPlume
from moves.status_moves.fire_moves.pyro_ball import PyroBall
from moves.status_moves.fire_moves.sacred_fire import SacredFire
from moves.status_moves.fire_moves.searing_shot import SearingShot
from moves.status_moves.fire_moves.will_o_wisp import WillOWisp
from moves.status_moves.flying_moves.air_slash import AirSlash
from moves.status_moves.flying_moves.bounce import Bounce
from moves.status_moves.flying_moves.floaty_fall import FloatyFall
from moves.status_moves.flying_moves.sky_attack import SkyAttack
from moves.status_moves.ghost_moves.astonish import Astonish
from moves.status_moves.ghost_moves.lick import Lick
from moves.status_moves.grass_moves.grass_whistle import GrassWhistle
from moves.status_moves.grass_moves.needle_arm import NeedleArm
from moves.status_moves.grass_moves.petal_dance import PetalDance
from moves.status_moves.grass_moves.sleep_powder import SleepPowder
from moves.status_moves.grass_moves.spore import Spore
from moves.status_moves.ground_moves.bone_club import BoneClub
from moves.status_moves.ice_moves.blizzard import Blizzard
from moves.status_moves.ice_moves.freeze_dry import FreezeDry
from moves.status_moves.ice_moves.freeze_shock import FreezeShock
from moves.status_moves.ice_moves.ice_beam import IceBeam
from moves.status_moves.ice_moves.ice_burn import IceBurn
from moves.status_moves.ice_moves.ice_fang import IceFang
from moves.status_moves.ice_moves.ice_punch import IcePunch
from moves.status_moves.ice_moves.icicle_crash import IcicleCrash
from moves.status_moves.ice_moves.powder_snow import PowderSnow
from moves.status_moves.normal_moves.body_slam import BodySlam
from moves.status_moves.normal_moves.headbutt import Headbutt
from moves.status_moves.normal_moves.hyper_fang import HyperFang
from moves.status_moves.normal_moves.lovely_kiss import LovelyKiss
from moves.status_moves.normal_moves.sing import Sing
from moves.status_moves.normal_moves.snore import Snore
from moves.status_moves.normal_moves.stomp import Stomp
from moves.status_moves.normal_moves.thrash import Thrash
from moves.status_moves.normal_moves.tri_attack import TriAttack
from moves.status_moves.normal_moves.yawn import Yawn
from moves.status_moves.poison_moves.cross_poison import CrossPoison
from moves.status_moves.poison_moves.gunk_shot import GunkShot
from moves.status_moves.poison_moves.poison_fang import PoisonFang
from moves.status_moves.poison_moves.poison_tail import PoisonTail
from moves.status_moves.poison_moves.shell_side_arm import ShellSideArm
from moves.status_moves.poison_moves.sludge import Sludge
from moves.status_moves.poison_moves.sludge_bomb import SludgeBomb
from moves.status_moves.poison_moves.sludge_wave import SludgeWave
from moves.status_moves.poison_moves.smog import Smog
from moves.status_moves.psychic_moves.extrasensory import Extrasensory
from moves.status_moves.psychic_moves.freezing_glare import FreezingGlare
from moves.status_moves.psychic_moves.heart_stamp import HeartStamp
from moves.status_moves.psychic_moves.hypnosis import Hypnosis
from moves.status_moves.psychic_moves.zen_headbutt import ZenHeadbutt
from moves.status_moves.rock_moves.rock_slide import RockSlide
from moves.status_moves.steel_moves.double_iron_bash import DoubleIronBash
from moves.status_moves.steel_moves.iron_head import IronHead
from moves.status_moves.water_moves.scald import Scald
from moves.status_moves.water_moves.splishy_splash import SplishySplash
from moves.status_moves.water_moves.steam_eruption import SteamEruption
from moves.status_moves.water_moves.waterfall import Waterfall
from moves.stat_modifier_moves.bug_moves.bug_buzz import BugBuzz
from moves.stat_modifier_moves.bug_moves.defend_order import DefendOrder
from moves.stat_modifier_moves.bug_moves.fell_stinger import FellStinger
from moves.stat_modifier_moves.bug_moves.lunge import Lunge
from moves.stat_modifier_moves.bug_moves.pounce import Pounce
from moves.stat_modifier_moves.bug_moves.quiver_dance import QuiverDance
from moves.stat_modifier_moves.bug_moves.silk_trap import SilkTrap
from moves.stat_modifier_moves.bug_moves.skitter_smack import SkitterSmack
from moves.stat_modifier_moves.bug_moves.sticky_web import StickyWeb
from moves.stat_modifier_moves.bug_moves.string_shot import StringShot
from moves.stat_modifier_moves.bug_moves.struggle_bug import StruggleBug
from moves.stat_modifier_moves.dark_moves.fake_tears import FakeTears
from moves.stat_modifier_moves.dark_moves.flatter import Flatter
from moves.stat_modifier_moves.dark_moves.hone_claws import HoneClaws
from moves.stat_modifier_moves.dark_moves.hyperspace_fury import HyperspaceFury
from moves.stat_modifier_moves.dark_moves.memento import Memento
from moves.stat_modifier_moves.dark_moves.nasty_plot import NastyPlot
from moves.stat_modifier_moves.dark_moves.obstruct import Obstruct
from moves.stat_modifier_moves.dark_moves.parting_shot import PartingShot
from moves.stat_modifier_moves.dark_moves.snarl import Snarl
from moves.stat_modifier_moves.dragon_moves.breaking_swipe import BreakingSwipe
from moves.stat_modifier_moves.dragon_moves.clanging_scales import ClangingScales
from moves.stat_modifier_moves.dragon_moves.clangorous_soul import ClangorousSoul
from moves.stat_modifier_moves.dragon_moves.draco_meteor import DracoMeteor
from moves.stat_modifier_moves.dragon_moves.dragon_dance import DragonDance
from moves.stat_modifier_moves.dragon_moves.scale_shot import ScaleShot
from moves.stat_modifier_moves.electric_moves.charge import Charge
from moves.stat_modifier_moves.electric_moves.eerie_impulse import EerieImpulse
from moves.stat_modifier_moves.electric_moves.electroweb import Electroweb
from moves.stat_modifier_moves.electric_moves.magnetic_flux import MagneticFlux
from moves.stat_modifier_moves.fairy_moves.aromatic_mist import AromaticMist
from moves.stat_modifier_moves.fairy_moves.baby_doll_eyes import BabyDollEyes
from moves.stat_modifier_moves.fairy_moves.charm import Charm
from moves.stat_modifier_moves.fairy_moves.decorate import Decorate
from moves.stat_modifier_moves.fairy_moves.fleur_cannon import FleurCannon
from moves.stat_modifier_moves.fairy_moves.flower_shield import FlowerShield
from moves.stat_modifier_moves.fairy_moves.geomancy import Geomancy
from moves.stat_modifier_moves.fairy_moves.spirit_break import SpiritBreak
from moves.stat_modifier_moves.fairy_moves.springtide_storm import SpringtideStorm
from moves.stat_modifier_moves.fighting_moves.bulk_up import BulkUp
from moves.stat_modifier_moves.fighting_moves.close_combat import CloseCombat
from moves.stat_modifier_moves.fighting_moves.hammer_arm import HammerArm
from moves.stat_modifier_moves.fighting_moves.low_sweep import LowSweep
from moves.stat_modifier_moves.fighting_moves.no_retreat import NoRetreat
from moves.stat_modifier_moves.fighting_moves.octolock import Octolock
from moves.stat_modifier_moves.fighting_moves.power_up_punch import PowerUpPunch
from moves.stat_modifier_moves.fighting_moves.superpower import Superpower
from moves.stat_modifier_moves.fire_moves.armor_cannon import ArmorCannon
from moves.stat_modifier_moves.fire_moves.fire_lash import FireLash
from moves.stat_modifier_moves.fire_moves.flame_charge import FlameCharge
from moves.stat_modifier_moves.fire_moves.mystical_fire import MysticalFire
from moves.stat_modifier_moves.fire_moves.overheat import Overheat
from moves.stat_modifier_moves.fire_moves.v_create import Vcreate
from moves.stat_modifier_moves.flying_moves.defog import Defog
from moves.stat_modifier_moves.flying_moves.dragon_ascent import DragonAscent
from moves.stat_modifier_moves.flying_moves.feather_dance import FeatherDance
from moves.stat_modifier_moves.grass_moves.apple_acid import AppleAcid
from moves.stat_modifier_moves.grass_moves.cotton_guard import CottonGuard
from moves.stat_modifier_moves.grass_moves.cotton_spore import CottonSpore
from moves.stat_modifier_moves.grass_moves.drum_beating import DrumBeating
from moves.stat_modifier_moves.grass_moves.grav_apple import GravApple
from moves.stat_modifier_moves.grass_moves.leaf_storm import LeafStorm
from moves.stat_modifier_moves.grass_moves.spicy_extract import SpicyExtract
from moves.stat_modifier_moves.grass_moves.strength_sap import StrengthSap
from moves.stat_modifier_moves.ground_moves.bulldoze import Bulldoze
from moves.stat_modifier_moves.ground_moves.headlong_rush import HeadlongRush
from moves.stat_modifier_moves.ground_moves.mud_shot import MudShot
from moves.stat_modifier_moves.ground_moves.mud_slap import MudSlap
from moves.stat_modifier_moves.ground_moves.rototiller import Rototiller
from moves.stat_modifier_moves.ground_moves.sand_attack import SandAttack
from moves.stat_modifier_moves.ice_moves.glaciate import Glaciate
from moves.stat_modifier_moves.ice_moves.ice_hammer import IceHammer
from moves.stat_modifier_moves.ice_moves.icy_wind import IcyWind
from moves.stat_modifier_moves.ice_moves.mountain_gale import MountainGale
from moves.stat_modifier_moves.ice_moves.snowscape import Snowscape
from moves.stat_modifier_moves.normal_moves.acupressure import Acupressure
from moves.stat_modifier_moves.normal_moves.belly_drum import BellyDrum
from moves.stat_modifier_moves.normal_moves.captivate import Captivate
from moves.stat_modifier_moves.normal_moves.confide import Confide
from moves.stat_modifier_moves.normal_moves.defense_curl import DefenseCurl
from moves.stat_modifier_moves.normal_moves.double_team import DoubleTeam
from moves.stat_modifier_moves.normal_moves.extreme_evoboost import ExtremeEvoboost
from moves.stat_modifier_moves.normal_moves.fillet_away import FilletAway
from moves.stat_modifier_moves.normal_moves.flash import Flash
from moves.stat_modifier_moves.normal_moves.growl import Growl
from moves.stat_modifier_moves.normal_moves.growth import Growth
from moves.stat_modifier_moves.normal_moves.harden import Harden
from moves.stat_modifier_moves.normal_moves.howl import Howl
from moves.stat_modifier_moves.normal_moves.leer import Leer
from moves.stat_modifier_moves.normal_moves.minimize import Minimize
from moves.stat_modifier_moves.normal_moves.noble_roar import NobleRoar
from moves.stat_modifier_moves.normal_moves.play_nice import PlayNice
from moves.stat_modifier_moves.normal_moves.rage import Rage
from moves.stat_modifier_moves.normal_moves.rapid_spin import RapidSpin
from moves.stat_modifier_moves.normal_moves.scary_face import ScaryFace
from moves.stat_modifier_moves.normal_moves.screech import Screech
from moves.stat_modifier_moves.normal_moves.sharpen import Sharpen
from moves.stat_modifier_moves.normal_moves.shell_smash import ShellSmash
from moves.stat_modifier_moves.normal_moves.skull_bash import SkullBash
from moves.stat_modifier_moves.normal_moves.smokescreen import Smokescreen
from moves.stat_modifier_moves.normal_moves.stuff_cheeks import StuffCheeks
from moves.stat_modifier_moves.normal_moves.swagger import Swagger
from moves.stat_modifier_moves.normal_moves.sweet_scent import SweetScent
from moves.stat_modifier_moves.normal_moves.swords_dance import SwordsDance
from moves.stat_modifier_moves.poison_moves.acid_armor import AcidArmor
from moves.stat_modifier_moves.poison_moves.acid_spray import AcidSpray
from moves.stat_modifier_moves.poison_moves.coil import Coil
from moves.stat_modifier_moves.psychic_moves.agility import Agility
from moves.stat_modifier_moves.psychic_moves.amnesia import Amnesia
from moves.stat_modifier_moves.psychic_moves.barrier import Barrier
from moves.stat_modifier_moves.psychic_moves.calm_mind import CalmMind
from moves.stat_modifier_moves.psychic_moves.cosmic_power import CosmicPower
from moves.stat_modifier_moves.psychic_moves.esper_wing import EsperWing
from moves.stat_modifier_moves.psychic_moves.kinesis import Kinesis
from moves.stat_modifier_moves.psychic_moves.lumina_crash import LuminaCrash
from moves.stat_modifier_moves.psychic_moves.meditate import Meditate
from moves.stat_modifier_moves.psychic_moves.mystical_power import MysticalPower
from moves.stat_modifier_moves.psychic_moves.psycho_boost import PsychoBoost
from moves.stat_modifier_moves.psychic_moves.psyshield_bash import PsyshieldBash
from moves.stat_modifier_moves.rock_moves.rock_polish import RockPolish
from moves.stat_modifier_moves.rock_moves.rock_tomb import RockTomb
from moves.stat_modifier_moves.steel_moves.autotomize import Autotomize
from moves.stat_modifier_moves.steel_moves.iron_defense import IronDefense
from moves.stat_modifier_moves.steel_moves.king_shield import KingShield
from moves.stat_modifier_moves.steel_moves.make_it_rain import MakeItRain
from moves.stat_modifier_moves.steel_moves.metal_sound import MetalSound
from moves.stat_modifier_moves.steel_moves.shelter import Shelter
from moves.stat_modifier_moves.steel_moves.shift_gear import ShiftGear
from moves.stat_modifier_moves.steel_moves.spin_out import SpinOut
from moves.stat_modifier_moves.water_moves.aqua_step import AquaStep
from moves.stat_modifier_moves.water_moves.chilling_water import ChillingWater
from moves.steel_moves.anchor_shot import AnchorShot
from moves.steel_moves.behemoth_bash import BehemothBash
from moves.steel_moves.behemoth_blade import BehemothBlade
from moves.steel_moves.bullet_punch import BulletPunch
from moves.steel_moves.corkscrew_crash import CorkscrewCrash
from moves.steel_moves.doom_desire import DoomDesire
from moves.steel_moves.flash_cannon import FlashCannon
from moves.steel_moves.gear_grind import GearGrind
from moves.steel_moves.gear_up import GearUp
from moves.steel_moves.gigaton_hammer import GigatonHammer
from moves.steel_moves.gyro_ball import GyroBall
from moves.steel_moves.heavy_slam import HeavySlam
from moves.steel_moves.iron_tail import IronTail
from moves.steel_moves.magnet_bomb import MagnetBomb
from moves.steel_moves.metal_burst import MetalBurst
from moves.steel_moves.metal_claw import MetalClaw
from moves.steel_moves.meteor_mash import MeteorMash
from moves.steel_moves.mirror_shot import MirrorShot
from moves.steel_moves.searing_sunraze_smash import SearingSunrazeSmash
from moves.steel_moves.smart_strike import SmartStrike
from moves.steel_moves.steel_beam import SteelBeam
from moves.steel_moves.steel_roller import SteelRoller
from moves.steel_moves.steel_wing import SteelWing
from moves.steel_moves.sunsteel_strike import SunsteelStrike
from moves.water_moves.aqua_cutter import AquaCutter
from moves.water_moves.aqua_jet import AquaJet
from moves.water_moves.aqua_ring import AquaRing
from moves.water_moves.aqua_tail import AquaTail
from moves.water_moves.bouncy_bubble import BouncyBubble
from moves.water_moves.brine import Brine
from moves.water_moves.bubble import Bubble
from moves.water_moves.bubble_beam import BubbleBeam
from moves.water_moves.clamp import Clamp
from moves.water_moves.crabhammer import Crabhammer
from moves.water_moves.dive import Dive
from moves.water_moves.fishious_rend import FishiousRend
from moves.water_moves.flip_turn import FlipTurn
from moves.water_moves.hydro_cannon import HydroCannon
from moves.water_moves.hydro_pump import HydroPump
from moves.water_moves.hydro_steam import HydroSteam
from moves.water_moves.hydro_vortex import HydroVortex
from moves.water_moves.jet_punch import JetPunch
from moves.water_moves.life_dew import LifeDew
from moves.water_moves.liquidation import Liquidation
from moves.water_moves.muddy_water import MuddyWater
from moves.water_moves.oceanic_operetta import OceanicOperetta
from moves.water_moves.octazooka import Octazooka
from moves.water_moves.origin_pulse import OriginPulse
from moves.water_moves.rain_dance import RainDance
from moves.water_moves.razor_shell import RazorShell
from moves.water_moves.snipe_shot import SnipeShot
from moves.water_moves.soak import Soak
from moves.water_moves.sparkling_aria import SparklingAria
from moves.water_moves.surf import Surf
from moves.water_moves.surging_strikes import SurgingStrikes
from moves.water_moves.triple_dive import TripleDive
from moves.water_moves.water_gun import WaterGun
from moves.water_moves.water_pledge import WaterPledge
from moves.water_moves.water_pulse import WaterPulse
from moves.water_moves.water_shuriken import WaterShuriken
from moves.water_moves.water_sport import WaterSport
from moves.water_moves.water_spout import WaterSpout
from moves.water_moves.wave_crash import WaveCrash
from moves.water_moves.whirlpool import Whirlpool
from moves.water_moves.withdraw import Withdraw

from moves.move import Move
from moves.enum_moves import Moves

class MoveFactory:
    @staticmethod
    def create_move(move: Moves) -> Move:
        if isinstance(move, str):
            move = Moves[move.upper()]

        if move == Moves.ATTACK_ORDER:
            return AttackOrder()
        elif move == Moves.BUG_BITE:
            return AttackOrder()
        elif move == Moves.FIRST_IMPRESSION:
            return BugBite()
        elif move == Moves.FURY_CUTTER:
            return FirstImpression()
        elif move == Moves.HEAL_ORDER:
            return FuryCutter()
        elif move == Moves.INFESTATION:
            return HealOrder()
        elif move == Moves.LEECH_LIFE:
            return Infestation()
        elif move == Moves.MEGAHORN:
            return LeechLife()
        elif move == Moves.PIN_MISSILE:
            return Megahorn()
        elif move == Moves.POLLEN_PUFF:
            return PinMissile()
        elif move == Moves.POWDER:
            return PollenPuff()
        elif move == Moves.RAGE_POWDER:
            return Powder()
        elif move == Moves.SAVAGE_SPIN_OUT:
            return RagePowder()
        elif move == Moves.SIGNAL_BEAM:
            return SavageSpinOut()
        elif move == Moves.SILVER_WIND:
            return SignalBeam()
        elif move == Moves.SPIDER_WEB:
            return SilverWind()
        elif move == Moves.TAIL_GLOW:
            return SpiderWeb()
        elif move == Moves.U_TURN:
            return TailGlow()
        elif move == Moves.X_SCISSOR:
            return Uturn()
        elif move == Moves.ASSURANCE:
            return XScissor()
        elif move == Moves.BADDY_BAD:
            return Assurance()
        elif move == Moves.BEAT_UP:
            return BaddyBad()
        elif move == Moves.BLACK_HOLE_ECLIPSE:
            return BeatUp()
        elif move == Moves.BRUTAL_SWING:
            return BlackHoleEclipse()
        elif move == Moves.CEASELESS_EDGE:
            return BrutalSwing()
        elif move == Moves.COMEUPPANCE:
            return CeaselessEdge()
        elif move == Moves.CRUNCH:
            return Comeuppance()
        elif move == Moves.DARKEST_LARIAT:
            return Crunch()
        elif move == Moves.DARK_VOID:
            return DarkestLariat()
        elif move == Moves.EMBARGO:
            return DarkVoid()
        elif move == Moves.FALSE_SURRENDER:
            return Embargo()
        elif move == Moves.FEINT_ATTACK:
            return FalseSurrender()
        elif move == Moves.FLING:
            return FeintAttack()
        elif move == Moves.FOUL_PLAY:
            return Fling()
        elif move == Moves.JAW_LOCK:
            return FoulPlay()
        elif move == Moves.KNOCK_OFF:
            return JawLock()
        elif move == Moves.KOWTOW_CLEAVE:
            return KnockOff()
        elif move == Moves.LASH_OUT:
            return KowtowCleave()
        elif move == Moves.MALICIOUS_MOONSAULT:
            return LashOut()
        elif move == Moves.NIGHT_DAZE:
            return MaliciousMoonsault()
        elif move == Moves.NIGHT_SLASH:
            return NightDaze()
        elif move == Moves.PAYBACK:
            return NightSlash()
        elif move == Moves.POWER_TRIP:
            return Payback()
        elif move == Moves.PUNISHMENT:
            return PowerTrip()
        elif move == Moves.PURSUIT:
            return Punishment()
        elif move == Moves.QUASH:
            return Pursuit()
        elif move == Moves.RUINATION:
            return Quash()
        elif move == Moves.SNATCH:
            return Ruination()
        elif move == Moves.SUCKER_PUNCH:
            return Snatch()
        elif move == Moves.SWITCHEROO:
            return SuckerPunch()
        elif move == Moves.THIEF:
            return Switcheroo()
        elif move == Moves.THROAT_CHOP:
            return Thief()
        elif move == Moves.TORMENT:
            return ThroatChop()
        elif move == Moves.WICKED_BLOW:
            return Torment()
        elif move == Moves.WICKED_TORQUE:
            return WickedBlow()
        elif move == Moves.CLANGOROUS_SOULBLAZE:
            return WickedTorque()
        elif move == Moves.CORE_ENFORCER:
            return ClangorousSoulblaze()
        elif move == Moves.DEVASTATING_DRAKE:
            return CoreEnforcer()
        elif move == Moves.DRAGON_CLAW:
            return DevastatingDrake()
        elif move == Moves.DRAGON_DARTS:
            return DragonClaw()
        elif move == Moves.DRAGON_ENERGY:
            return DragonDarts()
        elif move == Moves.DRAGON_HAMMER:
            return DragonEnergy()
        elif move == Moves.DRAGON_PULSE:
            return DragonHammer()
        elif move == Moves.DRAGON_RAGE:
            return DragonPulse()
        elif move == Moves.DRAGON_TAIL:
            return DragonRage()
        elif move == Moves.DUAL_CHOP:
            return DragonTail()
        elif move == Moves.DYNAMAX_CANNON:
            return DualChop()
        elif move == Moves.ETERNABEAM:
            return DynamaxCannon()
        elif move == Moves.GLAIVE_RUSH:
            return Eternabeam()
        elif move == Moves.ORDER_UP:
            return GlaiveRush()
        elif move == Moves.ROAR_OF_TIME:
            return OrderUp()
        elif move == Moves.SPACIAL_REND:
            return RoarofTime()
        elif move == Moves.AURA_WHEEL:
            return SpacialRend()
        elif move == Moves.BOLT_BEAK:
            return AuraWheel()
        elif move == Moves.BUZZY_BUZZ:
            return BoltBeak()
        elif move == Moves.CATASTROPIKA:
            return BuzzyBuzz()
        elif move == Moves.CHARGE_BEAM:
            return Catastropika()
        elif move == Moves.DOUBLE_SHOCK:
            return ChargeBeam()
        elif move == Moves.ELECTRIFY:
            return DoubleShock()
        elif move == Moves.ELECTRO_BALL:
            return Electrify()
        elif move == Moves.ELECTRO_DRIFT:
            return ElectroBall()
        elif move == Moves.FUSION_BOLT:
            return ElectroDrift()
        elif move == Moves.GIGAVOLT_HAVOC:
            return FusionBolt()
        elif move == Moves.ION_DELUGE:
            return GigavoltHavoc()
        elif move == Moves.MAGNET_RISE:
            return IonDeluge()
        elif move == Moves.NUZZLE:
            return MagnetRise()
        elif move == Moves.OVERDRIVE:
            return Nuzzle()
        elif move == Moves.PARABOLIC_CHARGE:
            return Overdrive()
        elif move == Moves.PIKA_PAPOW:
            return ParabolicCharge()
        elif move == Moves.PLASMA_FISTS:
            return PikaPapow()
        elif move == Moves.RISING_VOLTAGE:
            return PlasmaFists()
        elif move == Moves.SHOCK_WAVE:
            return RisingVoltage()
        elif move == Moves.STOKED_SPARKSURFER:
            return ShockWave()
        elif move == Moves.THUNDER_CAGE:
            return StokedSparksurfer()
        elif move == Moves.THUNDER_WAVE:
            return ThunderCage()
        elif move == Moves.VOLT_SWITCH:
            return ThunderWave()
        elif move == Moves.WILDBOLT_STORM:
            return VoltSwitch()
        elif move == Moves.WILD_CHARGE:
            return WildboltStorm()
        elif move == Moves.ZAP_CANNON:
            return WildCharge()
        elif move == Moves.ZIPPY_ZAP:
            return ZapCannon()
        elif move == Moves.CRAFTY_SHIELD:
            return ZippyZap()
        elif move == Moves.DAZZLING_GLEAM:
            return CraftyShield()
        elif move == Moves.DISARMING_VOICE:
            return DazzlingGleam()
        elif move == Moves.DRAINING_KISS:
            return DisarmingVoice()
        elif move == Moves.FAIRY_LOCK:
            return DrainingKiss()
        elif move == Moves.FAIRY_WIND:
            return FairyLock()
        elif move == Moves.FLORAL_HEALING:
            return FairyWind()
        elif move == Moves.GUARDIAN_OF_ALOLA:
            return FloralHealing()
        elif move == Moves.LIGHT_OF_RUIN:
            return GuardianofAlola()
        elif move == Moves.MAGICAL_TORQUE:
            return LightofRuin()
        elif move == Moves.MISTY_EXPLOSION:
            return MagicalTorque()
        elif move == Moves.MISTY_TERRAIN:
            return MistyExplosion()
        elif move == Moves.MOONBLAST:
            return MistyTerrain()
        elif move == Moves.MOONLIGHT:
            return Moonblast()
        elif move == Moves.NATURE_MADNESS:
            return Moonlight()
        elif move == Moves.PLAY_ROUGH:
            return NatureMadness()
        elif move == Moves.SPARKLY_SWIRL:
            return PlayRough()
        elif move == Moves.STRANGE_STEAM:
            return SparklySwirl()
        elif move == Moves.SWEET_KISS:
            return StrangeSteam()
        elif move == Moves.TWINKLE_TACKLE:
            return SweetKiss()
        elif move == Moves.ARM_THRUST:
            return TwinkleTackle()
        elif move == Moves.AURA_SPHERE:
            return ArmThrust()
        elif move == Moves.AXE_KICK:
            return AuraSphere()
        elif move == Moves.BODY_PRESS:
            return AxeKick()
        elif move == Moves.BRICK_BREAK:
            return BodyPress()
        elif move == Moves.CIRCLE_THROW:
            return BrickBreak()
        elif move == Moves.COACHING:
            return CircleThrow()
        elif move == Moves.COLLISION_COURSE:
            return Coaching()
        elif move == Moves.COMBAT_TORQUE:
            return CollisionCourse()
        elif move == Moves.COUNTER:
            return CombatTorque()
        elif move == Moves.CROSS_CHOP:
            return Counter()
        elif move == Moves.DETECT:
            return CrossChop()
        elif move == Moves.DOUBLE_KICK:
            return Detect()
        elif move == Moves.DRAIN_PUNCH:
            return DoubleKick()
        elif move == Moves.DYNAMIC_PUNCH:
            return DrainPunch()
        elif move == Moves.FINAL_GAMBIT:
            return DynamicPunch()
        elif move == Moves.FLYING_PRESS:
            return FinalGambit()
        elif move == Moves.FOCUS_BLAST:
            return FlyingPress()
        elif move == Moves.FOCUS_PUNCH:
            return FocusBlast()
        elif move == Moves.HIGH_JUMP_KICK:
            return FocusPunch()
        elif move == Moves.JUMP_KICK:
            return HighJumpKick()
        elif move == Moves.KARATE_CHOP:
            return JumpKick()
        elif move == Moves.LOW_KICK:
            return KarateChop()
        elif move == Moves.MACH_PUNCH:
            return LowKick()
        elif move == Moves.MAT_BLOCK:
            return MachPunch()
        elif move == Moves.METEOR_ASSAULT:
            return MatBlock()
        elif move == Moves.QUICK_GUARD:
            return MeteorAssault()
        elif move == Moves.REVENGE:
            return QuickGuard()
        elif move == Moves.REVERSAL:
            return Revenge()
        elif move == Moves.ROCK_SMASH:
            return Reversal()
        elif move == Moves.SACRED_SWORD:
            return RockSmash()
        elif move == Moves.SECRET_SWORD:
            return SacredSword()
        elif move == Moves.SEISMIC_TOSS:
            return SecretSword()
        elif move == Moves.SKY_UPPERCUT:
            return SeismicToss()
        elif move == Moves.STORM_THROW:
            return SkyUppercut()
        elif move == Moves.SUBMISSION:
            return StormThrow()
        elif move == Moves.THUNDEROUS_KICK:
            return Submission()
        elif move == Moves.TRIPLE_ARROWS:
            return ThunderousKick()
        elif move == Moves.TRIPLE_KICK:
            return TripleArrows()
        elif move == Moves.VACUUM_WAVE:
            return TripleKick()
        elif move == Moves.VICTORY_DANCE:
            return VacuumWave()
        elif move == Moves.VITAL_THROW:
            return VictoryDance()
        elif move == Moves.WAKE_UP_SLAP:
            return VitalThrow()
        elif move == Moves.BITTER_BLADE:
            return WakeUpSlap()
        elif move == Moves.BLAST_BURN:
            return BitterBlade()
        elif move == Moves.BLAZING_TORQUE:
            return BlastBurn()
        elif move == Moves.BURNING_JEALOUSY:
            return BlazingTorque()
        elif move == Moves.BURN_UP:
            return BurningJealousy()
        elif move == Moves.ERUPTION:
            return BurnUp()
        elif move == Moves.FIERY_DANCE:
            return Eruption()
        elif move == Moves.FIRE_PLEDGE:
            return FieryDance()
        elif move == Moves.FIRE_SPIN:
            return FirePledge()
        elif move == Moves.FLAME_BURST:
            return FireSpin()
        elif move == Moves.FUSION_FLARE:
            return FlameBurst()
        elif move == Moves.HEAT_CRASH:
            return FusionFlare()
        elif move == Moves.INCINERATE:
            return HeatCrash()
        elif move == Moves.INFERNO:
            return Incinerate()
        elif move == Moves.INFERNO_OVERDRIVE:
            return Inferno()
        elif move == Moves.MAGMA_STORM:
            return InfernoOverdrive()
        elif move == Moves.MIND_BLOWN:
            return MagmaStorm()
        elif move == Moves.RAGING_FURY:
            return MindBlown()
        elif move == Moves.SHELL_TRAP:
            return RagingFury()
        elif move == Moves.SIZZLY_SLIDE:
            return ShellTrap()
        elif move == Moves.SUNNY_DAY:
            return SizzlySlide()
        elif move == Moves.TORCH_SONG:
            return SunnyDay()
        elif move == Moves.ACROBATICS:
            return TorchSong()
        elif move == Moves.AERIAL_ACE:
            return Acrobatics()
        elif move == Moves.AEROBLAST:
            return AerialAce()
        elif move == Moves.AIR_CUTTER:
            return Aeroblast()
        elif move == Moves.BEAK_BLAST:
            return AirCutter()
        elif move == Moves.BLEAKWIND_STORM:
            return BeakBlast()
        elif move == Moves.BRAVE_BIRD:
            return BleakwindStorm()
        elif move == Moves.CHATTER:
            return BraveBird()
        elif move == Moves.DRILL_PECK:
            return Chatter()
        elif move == Moves.DUAL_WINGBEAT:
            return DrillPeck()
        elif move == Moves.FLY:
            return DualWingbeat()
        elif move == Moves.GUST:
            return Fly()
        elif move == Moves.HURRICANE:
            return Gust()
        elif move == Moves.MIRROR_MOVE:
            return Hurricane()
        elif move == Moves.OBLIVION_WING:
            return MirrorMove()
        elif move == Moves.PECK:
            return OblivionWing()
        elif move == Moves.PLUCK:
            return Peck()
        elif move == Moves.ROOST:
            return Pluck()
        elif move == Moves.SKY_DROP:
            return Roost()
        elif move == Moves.SUPERSONIC_SKYSTRIKE:
            return SkyDrop()
        elif move == Moves.TAILWIND:
            return SupersonicSkystrike()
        elif move == Moves.WING_ATTACK:
            return Tailwind()
        elif move == Moves.ASTRAL_BARRAGE:
            return WingAttack()
        elif move == Moves.BITTER_MALICE:
            return AstralBarrage()
        elif move == Moves.CONFUSE_RAY:
            return BitterMalice()
        elif move == Moves.CURSE:
            return ConfuseRay()
        elif move == Moves.DESTINY_BOND:
            return Curse()
        elif move == Moves.GRUDGE:
            return DestinyBond()
        elif move == Moves.HEX:
            return Grudge()
        elif move == Moves.INFERNAL_PARADE:
            return Hex()
        elif move == Moves.LAST_RESPECTS:
            return InfernalParade()
        elif move == Moves.MENACING_MOONRAZE_MAELSTROM:
            return LastRespects()
        elif move == Moves.MOONGEIST_BEAM:
            return MenacingMoonrazeMaelstrom()
        elif move == Moves.NIGHTMARE:
            return MoongeistBeam()
        elif move == Moves.NIGHT_SHADE:
            return Nightmare()
        elif move == Moves.OMINOUS_WIND:
            return NightShade()
        elif move == Moves.PHANTOM_FORCE:
            return OminousWind()
        elif move == Moves.RAGE_FIST:
            return PhantomForce()
        elif move == Moves.SHADOW_BALL:
            return RageFist()
        elif move == Moves.SHADOW_BONE:
            return ShadowBall()
        elif move == Moves.SHADOW_CLAW:
            return ShadowBone()
        elif move == Moves.SHADOW_FORCE:
            return ShadowClaw()
        elif move == Moves.SHADOW_PUNCH:
            return ShadowForce()
        elif move == Moves.SHADOW_SNEAK:
            return ShadowPunch()
        elif move == Moves.SINISTER_ARROW_RAID:
            return ShadowSneak()
        elif move == Moves.SPECTRAL_THIEF:
            return SinisterArrowRaid()
        elif move == Moves.SPIRIT_SHACKLE:
            return SpectralThief()
        elif move == Moves.SPITE:
            return SpiritShackle()
        elif move == Moves.TRICK_OR_TREAT:
            return Spite()
        elif move == Moves.ABSORB:
            return TrickorTreat()
        elif move == Moves.AROMATHERAPY:
            return Absorb()
        elif move == Moves.BLOOM_DOOM:
            return Aromatherapy()
        elif move == Moves.BRANCH_POKE:
            return BloomDoom()
        elif move == Moves.BULLET_SEED:
            return BranchPoke()
        elif move == Moves.CHLOROBLAST:
            return BulletSeed()
        elif move == Moves.ENERGY_BALL:
            return Chloroblast()
        elif move == Moves.FLOWER_TRICK:
            return EnergyBall()
        elif move == Moves.FOREST_CURSE:
            return FlowerTrick()
        elif move == Moves.FRENZY_PLANT:
            return ForestCurse()
        elif move == Moves.GIGA_DRAIN:
            return FrenzyPlant()
        elif move == Moves.GRASSY_GLIDE:
            return GigaDrain()
        elif move == Moves.GRASSY_TERRAIN:
            return GrassyGlide()
        elif move == Moves.GRASS_KNOT:
            return GrassyTerrain()
        elif move == Moves.GRASS_PLEDGE:
            return GrassKnot()
        elif move == Moves.HORN_LEECH:
            return GrassPledge()
        elif move == Moves.INGRAIN:
            return HornLeech()
        elif move == Moves.JUNGLE_HEALING:
            return Ingrain()
        elif move == Moves.LEAFAGE:
            return JungleHealing()
        elif move == Moves.LEAF_BLADE:
            return Leafage()
        elif move == Moves.LEAF_TORNADO:
            return LeafBlade()
        elif move == Moves.LEECH_SEED:
            return LeafTornado()
        elif move == Moves.MAGICAL_LEAF:
            return LeechSeed()
        elif move == Moves.MEGA_DRAIN:
            return MagicalLeaf()
        elif move == Moves.PETAL_BLIZZARD:
            return MegaDrain()
        elif move == Moves.POWER_WHIP:
            return PetalBlizzard()
        elif move == Moves.RAZOR_LEAF:
            return PowerWhip()
        elif move == Moves.SAPPY_SEED:
            return RazorLeaf()
        elif move == Moves.SEED_BOMB:
            return SappySeed()
        elif move == Moves.SEED_FLARE:
            return SeedBomb()
        elif move == Moves.SNAP_TRAP:
            return SeedFlare()
        elif move == Moves.SOLAR_BEAM:
            return SnapTrap()
        elif move == Moves.SOLAR_BLADE:
            return SolarBeam()
        elif move == Moves.SPIKY_SHIELD:
            return SolarBlade()
        elif move == Moves.STUN_SPORE:
            return SpikyShield()
        elif move == Moves.SYNTHESIS:
            return StunSpore()
        elif move == Moves.TRAILBLAZE:
            return Synthesis()
        elif move == Moves.TROP_KICK:
            return Trailblaze()
        elif move == Moves.VINE_WHIP:
            return TropKick()
        elif move == Moves.WOOD_HAMMER:
            return VineWhip()
        elif move == Moves.WORRY_SEED:
            return WoodHammer()
        elif move == Moves.BONEMERANG:
            return WorrySeed()
        elif move == Moves.BONE_RUSH:
            return Bonemerang()
        elif move == Moves.DIG:
            return BoneRush()
        elif move == Moves.DRILL_RUN:
            return Dig()
        elif move == Moves.EARTHQUAKE:
            return DrillRun()
        elif move == Moves.EARTH_POWER:
            return Earthquake()
        elif move == Moves.FISSURE:
            return EarthPower()
        elif move == Moves.HIGH_HORSEPOWER:
            return Fissure()
        elif move == Moves.LAND_WRATH:
            return HighHorsepower()
        elif move == Moves.MAGNITUDE:
            return LandWrath()
        elif move == Moves.MUD_BOMB:
            return Magnitude()
        elif move == Moves.MUD_SPORT:
            return MudBomb()
        elif move == Moves.PRECIPICE_BLADES:
            return MudSport()
        elif move == Moves.SANDSEAR_STORM:
            return PrecipiceBlades()
        elif move == Moves.SAND_TOMB:
            return SandsearStorm()
        elif move == Moves.SCORCHING_SANDS:
            return SandTomb()
        elif move == Moves.SHORE_UP:
            return ScorchingSands()
        elif move == Moves.SPIKES:
            return ShoreUp()
        elif move == Moves.STOMPING_TANTRUM:
            return Spikes()
        elif move == Moves.TECTONIC_RAGE:
            return StompingTantrum()
        elif move == Moves.THOUSAND_ARROWS:
            return TectonicRage()
        elif move == Moves.THOUSAND_WAVES:
            return ThousandArrows()
        elif move == Moves.AURORA_BEAM:
            return ThousandWaves()
        elif move == Moves.AURORA_VEIL:
            return AuroraBeam()
        elif move == Moves.AVALANCHE:
            return AuroraVeil()
        elif move == Moves.CHILLY_RECEPTION:
            return Avalanche()
        elif move == Moves.FREEZY_FROST:
            return ChillyReception()
        elif move == Moves.FROST_BREATH:
            return FreezyFrost()
        elif move == Moves.GLACIAL_LANCE:
            return FrostBreath()
        elif move == Moves.HAIL:
            return GlacialLance()
        elif move == Moves.HAZE:
            return Hail()
        elif move == Moves.ICE_BALL:
            return Haze()
        elif move == Moves.ICE_SHARD:
            return IceBall()
        elif move == Moves.ICE_SPINNER:
            return IceShard()
        elif move == Moves.ICICLE_SPEAR:
            return IceSpinner()
        elif move == Moves.MIST:
            return IcicleSpear()
        elif move == Moves.SHEER_COLD:
            return Mist()
        elif move == Moves.SUBZERO_SLAMMER:
            return SheerCold()
        elif move == Moves.TRIPLE_AXEL:
            return SubzeroSlammer()
        elif move == Moves.AFTER_YOU:
            return TripleAxel()
        elif move == Moves.ASSIST:
            return AfterYou()
        elif move == Moves.ATTRACT:
            return Assist()
        elif move == Moves.BARRAGE:
            return Attract()
        elif move == Moves.BATON_PASS:
            return Barrage()
        elif move == Moves.BESTOW:
            return BatonPass()
        elif move == Moves.BIDE:
            return Bestow()
        elif move == Moves.BIND:
            return Bide()
        elif move == Moves.BLOCK:
            return Bind()
        elif move == Moves.BOOMBURST:
            return Block()
        elif move == Moves.BREAKNECK_BLITZ:
            return Boomburst()
        elif move == Moves.CAMOUFLAGE:
            return BreakneckBlitz()
        elif move == Moves.CELEBRATE:
            return Camouflage()
        elif move == Moves.CHIP_AWAY:
            return Celebrate()
        elif move == Moves.COMET_PUNCH:
            return ChipAway()
        elif move == Moves.CONSTRICT:
            return CometPunch()
        elif move == Moves.CONVERSION:
            return Constrict()
        elif move == Moves.CONVERSION_2:
            return Conversion()
        elif move == Moves.COPYCAT:
            return Conversion2()
        elif move == Moves.COURT_CHANGE:
            return Copycat()
        elif move == Moves.COVET:
            return CourtChange()
        elif move == Moves.CRUSH_CLAW:
            return Covet()
        elif move == Moves.CRUSH_GRIP:
            return CrushClaw()
        elif move == Moves.CUT:
            return CrushGrip()
        elif move == Moves.DISABLE:
            return Cut()
        elif move == Moves.DIZZY_PUNCH:
            return Disable()
        elif move == Moves.DOODLE:
            return DizzyPunch()
        elif move == Moves.DOUBLE_EDGE:
            return Doodle()
        elif move == Moves.DOUBLE_HIT:
            return DoubleEdge()
        elif move == Moves.DOUBLE_SLAP:
            return DoubleHit()
        elif move == Moves.ECHOED_VOICE:
            return DoubleSlap()
        elif move == Moves.EGG_BOMB:
            return EchoedVoice()
        elif move == Moves.ENCORE:
            return EggBomb()
        elif move == Moves.ENDEAVOR:
            return Encore()
        elif move == Moves.ENDURE:
            return Endeavor()
        elif move == Moves.ENTRAINMENT:
            return Endure()
        elif move == Moves.EXPLOSION:
            return Entrainment()
        elif move == Moves.EXTREME_SPEED:
            return Explosion()
        elif move == Moves.FACADE:
            return ExtremeSpeed()
        elif move == Moves.FAKE_OUT:
            return Facade()
        elif move == Moves.FALSE_SWIPE:
            return FakeOut()
        elif move == Moves.FEINT:
            return FalseSwipe()
        elif move == Moves.FLAIL:
            return Feint()
        elif move == Moves.FOCUS_ENERGY:
            return Flail()
        elif move == Moves.FOLLOW_ME:
            return FocusEnergy()
        elif move == Moves.FORESIGHT:
            return FollowMe()
        elif move == Moves.FRUSTRATION:
            return Foresight()
        elif move == Moves.FURY_ATTACK:
            return Frustration()
        elif move == Moves.FURY_SWIPES:
            return FuryAttack()
        elif move == Moves.GIGA_IMPACT:
            return FurySwipes()
        elif move == Moves.GLARE:
            return GigaImpact()
        elif move == Moves.GUILLOTINE:
            return Glare()
        elif move == Moves.HAPPY_HOUR:
            return Guillotine()
        elif move == Moves.HEAD_CHARGE:
            return HappyHour()
        elif move == Moves.HEAL_BELL:
            return HeadCharge()
        elif move == Moves.HELPING_HAND:
            return HealBell()
        elif move == Moves.HIDDEN_POWER:
            return HelpingHand()
        elif move == Moves.HOLD_BACK:
            return HiddenPower()
        elif move == Moves.HOLD_HANDS:
            return HoldBack()
        elif move == Moves.HORN_ATTACK:
            return HoldHands()
        elif move == Moves.HORN_DRILL:
            return HornAttack()
        elif move == Moves.HYPER_BEAM:
            return HornDrill()
        elif move == Moves.HYPER_DRILL:
            return HyperBeam()
        elif move == Moves.HYPER_VOICE:
            return HyperDrill()
        elif move == Moves.JUDGMENT:
            return HyperVoice()
        elif move == Moves.LASER_FOCUS:
            return Judgment()
        elif move == Moves.LAST_RESORT:
            return LaserFocus()
        elif move == Moves.LOCK_ON:
            return LastResort()
        elif move == Moves.LUCKY_CHANT:
            return LockOn()
        elif move == Moves.MEAN_LOOK:
            return LuckyChant()
        elif move == Moves.MEGA_KICK:
            return MeanLook()
        elif move == Moves.MEGA_PUNCH:
            return MegaKick()
        elif move == Moves.METRONOME:
            return MegaPunch()
        elif move == Moves.ME_FIRST:
            return Metronome()
        elif move == Moves.MILK_DRINK:
            return MeFirst()
        elif move == Moves.MIMIC:
            return MilkDrink()
        elif move == Moves.MIND_READER:
            return Mimic()
        elif move == Moves.MORNING_SUN:
            return MindReader()
        elif move == Moves.MULTI_ATTACK:
            return MorningSun()
        elif move == Moves.NATURAL_GIFT:
            return MultiAttack()
        elif move == Moves.NATURE_POWER:
            return NaturalGift()
        elif move == Moves.ODOR_SLEUTH:
            return NaturePower()
        elif move == Moves.PAIN_SPLIT:
            return OdorSleuth()
        elif move == Moves.PAY_DAY:
            return PainSplit()
        elif move == Moves.PERISH_SONG:
            return PayDay()
        elif move == Moves.POPULATION_BOMB:
            return PerishSong()
        elif move == Moves.POUND:
            return PopulationBomb()
        elif move == Moves.POWER_SHIFT:
            return Pound()
        elif move == Moves.PRESENT:
            return PowerShift()
        elif move == Moves.PROTECT:
            return Present()
        elif move == Moves.PSYCH_UP:
            return Protect()
        elif move == Moves.PULVERIZING_PANCAKE:
            return PsychUp()
        elif move == Moves.QUICK_ATTACK:
            return PulverizingPancake()
        elif move == Moves.RAGING_BULL:
            return QuickAttack()
        elif move == Moves.RAZOR_WIND:
            return RagingBull()
        elif move == Moves.RECOVER:
            return RazorWind()
        elif move == Moves.RECYCLE:
            return Recover()
        elif move == Moves.REFLECT_TYPE:
            return Recycle()
        elif move == Moves.REFRESH:
            return ReflectType()
        elif move == Moves.RELIC_SONG:
            return Refresh()
        elif move == Moves.RETALIATE:
            return RelicSong()
        elif move == Moves.RETURN_:
            return Retaliate()
        elif move == Moves.REVELATION_DANCE:
            return Return()
        elif move == Moves.REVIVAL_BLESSING:
            return RevelationDance()
        elif move == Moves.ROAR:
            return RevivalBlessing()
        elif move == Moves.ROCK_CLIMB:
            return Roar()
        elif move == Moves.ROUND:
            return RockClimb()
        elif move == Moves.SAFEGUARD:
            return Round()
        elif move == Moves.SCRATCH:
            return Safeguard()
        elif move == Moves.SECRET_POWER:
            return Scratch()
        elif move == Moves.SELF_DESTRUCT:
            return SecretPower()
        elif move == Moves.SHED_TAIL:
            return SelfDestruct()
        elif move == Moves.SIMPLE_BEAM:
            return ShedTail()
        elif move == Moves.SKETCH:
            return SimpleBeam()
        elif move == Moves.SLACK_OFF:
            return Sketch()
        elif move == Moves.SLAM:
            return SlackOff()
        elif move == Moves.SLASH:
            return Slam()
        elif move == Moves.SLEEP_TALK:
            return Slash()
        elif move == Moves.SMELLING_SALTS:
            return SleepTalk()
        elif move == Moves.SOFT_BOILED:
            return SmellingSalts()
        elif move == Moves.SONIC_BOOM:
            return SoftBoiled()
        elif move == Moves.SPIKE_CANNON:
            return SonicBoom()
        elif move == Moves.SPIT_UP:
            return SpikeCannon()
        elif move == Moves.SPLASH:
            return SpitUp()
        elif move == Moves.SPOTLIGHT:
            return Splash()
        elif move == Moves.STOCKPILE:
            return Spotlight()
        elif move == Moves.STRENGTH:
            return Stockpile()
        elif move == Moves.STRUGGLE:
            return Strength()
        elif move == Moves.SUBSTITUTE:
            return Struggle()
        elif move == Moves.SUPERSONIC:
            return Substitute()
        elif move == Moves.SUPER_FANG:
            return Supersonic()
        elif move == Moves.SWALLOW:
            return SuperFang()
        elif move == Moves.SWIFT:
            return Swallow()
        elif move == Moves.TACKLE:
            return Swift()
        elif move == Moves.TAIL_SLAP:
            return Tackle()
        elif move == Moves.TAIL_WHIP:
            return TailSlap()
        elif move == Moves.TAKE_DOWN:
            return TailWhip()
        elif move == Moves.TEARFUL_LOOK:
            return TakeDown()
        elif move == Moves.TEATIME:
            return TearfulLook()
        elif move == Moves.TECHNO_BLAST:
            return Teatime()
        elif move == Moves.TEETER_DANCE:
            return TechnoBlast()
        elif move == Moves.TERA_BLAST:
            return TeeterDance()
        elif move == Moves.TERRAIN_PULSE:
            return TeraBlast()
        elif move == Moves.TICKLE:
            return TerrainPulse()
        elif move == Moves.TIDY_UP:
            return Tickle()
        elif move == Moves.TRANSFORM:
            return TidyUp()
        elif move == Moves.TRUMP_CARD:
            return Transform()
        elif move == Moves.UPROAR:
            return TrumpCard()
        elif move == Moves.VEEVEE_VOLLEY:
            return Uproar()
        elif move == Moves.VISE_GRIP:
            return VeeveeVolley()
        elif move == Moves.WEATHER_BALL:
            return ViseGrip()
        elif move == Moves.WHIRLWIND:
            return WeatherBall()
        elif move == Moves.WISH:
            return Whirlwind()
        elif move == Moves.WORK_UP:
            return Wish()
        elif move == Moves.WRAP:
            return WorkUp()
        elif move == Moves.WRING_OUT:
            return Wrap()
        elif move == Moves.ACID:
            return WringOut()
        elif move == Moves.ACID_DOWNPOUR:
            return Acid()
        elif move == Moves.BANEFUL_BUNKER:
            return AcidDownpour()
        elif move == Moves.BARB_BARRAGE:
            return BanefulBunker()
        elif move == Moves.BELCH:
            return BarbBarrage()
        elif move == Moves.CLEAR_SMOG:
            return Belch()
        elif move == Moves.CORROSIVE_GAS:
            return ClearSmog()
        elif move == Moves.DIRE_CLAW:
            return CorrosiveGas()
        elif move == Moves.GASTRO_ACID:
            return DireClaw()
        elif move == Moves.MORTAL_SPIN:
            return GastroAcid()
        elif move == Moves.NOXIOUS_TORQUE:
            return MortalSpin()
        elif move == Moves.POISON_GAS:
            return NoxiousTorque()
        elif move == Moves.POISON_JAB:
            return PoisonGas()
        elif move == Moves.POISON_POWDER:
            return PoisonJab()
        elif move == Moves.POISON_STING:
            return PoisonPowder()
        elif move == Moves.PURIFY:
            return PoisonSting()
        elif move == Moves.TOXIC:
            return Purify()
        elif move == Moves.TOXIC_SPIKES:
            return Toxic()
        elif move == Moves.TOXIC_THREAD:
            return ToxicSpikes()
        elif move == Moves.VENOM_DRENCH:
            return ToxicThread()
        elif move == Moves.VENOSHOCK:
            return VenomDrench()
        elif move == Moves.ALLY_SWITCH:
            return Venoshock()
        elif move == Moves.CONFUSION:
            return AllySwitch()
        elif move == Moves.DREAM_EATER:
            return Confusion()
        elif move == Moves.EERIE_SPELL:
            return DreamEater()
        elif move == Moves.EXPANDING_FORCE:
            return EerieSpell()
        elif move == Moves.FUTURE_SIGHT:
            return ExpandingForce()
        elif move == Moves.GENESIS_SUPERNOVA:
            return FutureSight()
        elif move == Moves.GLITZY_GLOW:
            return GenesisSupernova()
        elif move == Moves.GRAVITY:
            return GlitzyGlow()
        elif move == Moves.GUARD_SPLIT:
            return Gravity()
        elif move == Moves.GUARD_SWAP:
            return GuardSplit()
        elif move == Moves.HEALING_WISH:
            return GuardSwap()
        elif move == Moves.HEAL_BLOCK:
            return HealingWish()
        elif move == Moves.HEAL_PULSE:
            return HealBlock()
        elif move == Moves.HEART_SWAP:
            return HealPulse()
        elif move == Moves.HYPERSPACE_HOLE:
            return HeartSwap()
        elif move == Moves.IMPRISON:
            return HyperspaceHole()
        elif move == Moves.INSTRUCT:
            return Imprison()
        elif move == Moves.LIGHT_SCREEN:
            return Instruct()
        elif move == Moves.LIGHT_THAT_BURNS_THE_SKY:
            return LightScreen()
        elif move == Moves.LUNAR_BLESSING:
            return LightThatBurnstheSky()
        elif move == Moves.LUNAR_DANCE:
            return LunarBlessing()
        elif move == Moves.LUSTER_PURGE:
            return LunarDance()
        elif move == Moves.MAGIC_COAT:
            return LusterPurge()
        elif move == Moves.MAGIC_POWDER:
            return MagicCoat()
        elif move == Moves.MAGIC_ROOM:
            return MagicPowder()
        elif move == Moves.MIRACLE_EYE:
            return MagicRoom()
        elif move == Moves.MIRROR_COAT:
            return MiracleEye()
        elif move == Moves.MIST_BALL:
            return MirrorCoat()
        elif move == Moves.PHOTON_GEYSER:
            return MistBall()
        elif move == Moves.POWER_SPLIT:
            return PhotonGeyser()
        elif move == Moves.POWER_SWAP:
            return PowerSplit()
        elif move == Moves.POWER_TRICK:
            return PowerSwap()
        elif move == Moves.PRISMATIC_LASER:
            return PowerTrick()
        elif move == Moves.PSYBEAM:
            return PrismaticLaser()
        elif move == Moves.PSYBLADE:
            return Psybeam()
        elif move == Moves.PSYCHIC:
            return Psyblade()
        elif move == Moves.PSYCHIC_FANGS:
            return Psychic()
        elif move == Moves.PSYCHIC_TERRAIN:
            return PsychicFangs()
        elif move == Moves.PSYCHO_CUT:
            return PsychicTerrain()
        elif move == Moves.PSYCHO_SHIFT:
            return PsychoCut()
        elif move == Moves.PSYSHOCK:
            return PsychoShift()
        elif move == Moves.PSYSTRIKE:
            return Psyshock()
        elif move == Moves.PSYWAVE:
            return Psystrike()
        elif move == Moves.REFLECT:
            return Psywave()
        elif move == Moves.REST:
            return Reflect()
        elif move == Moves.ROLE_PLAY:
            return Rest()
        elif move == Moves.SHATTERED_PSYCHE:
            return RolePlay()
        elif move == Moves.SKILL_SWAP:
            return ShatteredPsyche()
        elif move == Moves.SPEED_SWAP:
            return SkillSwap()
        elif move == Moves.STORED_POWER:
            return SpeedSwap()
        elif move == Moves.SYNCHRONOISE:
            return StoredPower()
        elif move == Moves.TAKE_HEART:
            return Synchronoise()
        elif move == Moves.TELEKINESIS:
            return TakeHeart()
        elif move == Moves.TELEPORT:
            return Telekinesis()
        elif move == Moves.TRICK:
            return Teleport()
        elif move == Moves.TRICK_ROOM:
            return Trick()
        elif move == Moves.TWIN_BEAM:
            return TrickRoom()
        elif move == Moves.WONDER_ROOM:
            return TwinBeam()
        elif move == Moves.ACCELEROCK:
            return WonderRoom()
        elif move == Moves.ANCIENT_POWER:
            return Accelerock()
        elif move == Moves.CONTINENTAL_CRUSH:
            return AncientPower()
        elif move == Moves.DIAMOND_STORM:
            return ContinentalCrush()
        elif move == Moves.HEAD_SMASH:
            return DiamondStorm()
        elif move == Moves.METEOR_BEAM:
            return HeadSmash()
        elif move == Moves.POWER_GEM:
            return MeteorBeam()
        elif move == Moves.ROCK_BLAST:
            return PowerGem()
        elif move == Moves.ROCK_THROW:
            return RockBlast()
        elif move == Moves.ROCK_WRECKER:
            return RockThrow()
        elif move == Moves.ROLLOUT:
            return RockWrecker()
        elif move == Moves.SALT_CURE:
            return Rollout()
        elif move == Moves.SANDSTORM:
            return SaltCure()
        elif move == Moves.SMACK_DOWN:
            return Sandstorm()
        elif move == Moves.SPLINTERED_STORMSHARDS:
            return SmackDown()
        elif move == Moves.STEALTH_ROCK:
            return SplinteredStormshards()
        elif move == Moves.STONE_AXE:
            return StealthRock()
        elif move == Moves.STONE_EDGE:
            return StoneAxe()
        elif move == Moves.TAR_SHOT:
            return StoneEdge()
        elif move == Moves.WIDE_GUARD:
            return TarShot()
        elif move == Moves.STEAMROLLER:
            return WideGuard()
        elif move == Moves.TWINEEDLE:
            return Steamroller()
        elif move == Moves.BITE:
            return Twineedle()
        elif move == Moves.DARK_PULSE:
            return Bite()
        elif move == Moves.FIERY_WRATH:
            return DarkPulse()
        elif move == Moves.TAUNT:
            return FieryWrath()
        elif move == Moves.DRAGON_BREATH:
            return Taunt()
        elif move == Moves.DRAGON_RUSH:
            return DragonBreath()
        elif move == Moves.OUTRAGE:
            return DragonRush()
        elif move == Moves.TWISTER:
            return Outrage()
        elif move == Moves.BOLT_STRIKE:
            return Twister()
        elif move == Moves.DISCHARGE:
            return BoltStrike()
        elif move == Moves.SPARK:
            return Discharge()
        elif move == Moves.THUNDER:
            return Spark()
        elif move == Moves.THUNDERBOLT:
            return Thunder()
        elif move == Moves.THUNDER_FANG:
            return Thunderbolt()
        elif move == Moves.THUNDER_PUNCH:
            return ThunderFang()
        elif move == Moves.THUNDER_SHOCK:
            return ThunderPunch()
        elif move == Moves.VOLT_TACKLE:
            return ThunderShock()
        elif move == Moves.ZING_ZAP:
            return VoltTackle()
        elif move == Moves.FORCE_PALM:
            return ZingZap()
        elif move == Moves.ROLLING_KICK:
            return ForcePalm()
        elif move == Moves.BLAZE_KICK:
            return RollingKick()
        elif move == Moves.BLUE_FLARE:
            return BlazeKick()
        elif move == Moves.EMBER:
            return BlueFlare()
        elif move == Moves.FIRE_BLAST:
            return Ember()
        elif move == Moves.FIRE_FANG:
            return FireBlast()
        elif move == Moves.FIRE_PUNCH:
            return FireFang()
        elif move == Moves.FLAMETHROWER:
            return FirePunch()
        elif move == Moves.FLAME_WHEEL:
            return Flamethrower()
        elif move == Moves.FLARE_BLITZ:
            return FlameWheel()
        elif move == Moves.HEAT_WAVE:
            return FlareBlitz()
        elif move == Moves.LAVA_PLUME:
            return HeatWave()
        elif move == Moves.PYRO_BALL:
            return LavaPlume()
        elif move == Moves.SACRED_FIRE:
            return PyroBall()
        elif move == Moves.SEARING_SHOT:
            return SacredFire()
        elif move == Moves.WILL_O_WISP:
            return SearingShot()
        elif move == Moves.AIR_SLASH:
            return WillOWisp()
        elif move == Moves.BOUNCE:
            return AirSlash()
        elif move == Moves.FLOATY_FALL:
            return Bounce()
        elif move == Moves.SKY_ATTACK:
            return FloatyFall()
        elif move == Moves.ASTONISH:
            return SkyAttack()
        elif move == Moves.LICK:
            return Astonish()
        elif move == Moves.GRASS_WHISTLE:
            return Lick()
        elif move == Moves.NEEDLE_ARM:
            return GrassWhistle()
        elif move == Moves.PETAL_DANCE:
            return NeedleArm()
        elif move == Moves.SLEEP_POWDER:
            return PetalDance()
        elif move == Moves.SPORE:
            return SleepPowder()
        elif move == Moves.BONE_CLUB:
            return Spore()
        elif move == Moves.BLIZZARD:
            return BoneClub()
        elif move == Moves.FREEZE_DRY:
            return Blizzard()
        elif move == Moves.FREEZE_SHOCK:
            return FreezeDry()
        elif move == Moves.ICE_BEAM:
            return FreezeShock()
        elif move == Moves.ICE_BURN:
            return IceBeam()
        elif move == Moves.ICE_FANG:
            return IceBurn()
        elif move == Moves.ICE_PUNCH:
            return IceFang()
        elif move == Moves.ICICLE_CRASH:
            return IcePunch()
        elif move == Moves.POWDER_SNOW:
            return IcicleCrash()
        elif move == Moves.BODY_SLAM:
            return PowderSnow()
        elif move == Moves.HEADBUTT:
            return BodySlam()
        elif move == Moves.HYPER_FANG:
            return Headbutt()
        elif move == Moves.LOVELY_KISS:
            return HyperFang()
        elif move == Moves.SING:
            return LovelyKiss()
        elif move == Moves.SNORE:
            return Sing()
        elif move == Moves.STOMP:
            return Snore()
        elif move == Moves.THRASH:
            return Stomp()
        elif move == Moves.TRI_ATTACK:
            return Thrash()
        elif move == Moves.YAWN:
            return TriAttack()
        elif move == Moves.CROSS_POISON:
            return Yawn()
        elif move == Moves.GUNK_SHOT:
            return CrossPoison()
        elif move == Moves.POISON_FANG:
            return GunkShot()
        elif move == Moves.POISON_TAIL:
            return PoisonFang()
        elif move == Moves.SHELL_SIDE_ARM:
            return PoisonTail()
        elif move == Moves.SLUDGE:
            return ShellSideArm()
        elif move == Moves.SLUDGE_BOMB:
            return Sludge()
        elif move == Moves.SLUDGE_WAVE:
            return SludgeBomb()
        elif move == Moves.SMOG:
            return SludgeWave()
        elif move == Moves.EXTRASENSORY:
            return Smog()
        elif move == Moves.FREEZING_GLARE:
            return Extrasensory()
        elif move == Moves.HEART_STAMP:
            return FreezingGlare()
        elif move == Moves.HYPNOSIS:
            return HeartStamp()
        elif move == Moves.ZEN_HEADBUTT:
            return Hypnosis()
        elif move == Moves.ROCK_SLIDE:
            return ZenHeadbutt()
        elif move == Moves.DOUBLE_IRON_BASH:
            return RockSlide()
        elif move == Moves.IRON_HEAD:
            return DoubleIronBash()
        elif move == Moves.SCALD:
            return IronHead()
        elif move == Moves.SPLISHY_SPLASH:
            return Scald()
        elif move == Moves.STEAM_ERUPTION:
            return SplishySplash()
        elif move == Moves.WATERFALL:
            return SteamEruption()
        elif move == Moves.BUG_BUZZ:
            return Waterfall()
        elif move == Moves.DEFEND_ORDER:
            return BugBuzz()
        elif move == Moves.FELL_STINGER:
            return DefendOrder()
        elif move == Moves.LUNGE:
            return FellStinger()
        elif move == Moves.POUNCE:
            return Lunge()
        elif move == Moves.QUIVER_DANCE:
            return Pounce()
        elif move == Moves.SILK_TRAP:
            return QuiverDance()
        elif move == Moves.SKITTER_SMACK:
            return SilkTrap()
        elif move == Moves.STICKY_WEB:
            return SkitterSmack()
        elif move == Moves.STRING_SHOT:
            return StickyWeb()
        elif move == Moves.STRUGGLE_BUG:
            return StringShot()
        elif move == Moves.FAKE_TEARS:
            return StruggleBug()
        elif move == Moves.FLATTER:
            return FakeTears()
        elif move == Moves.HONE_CLAWS:
            return Flatter()
        elif move == Moves.HYPERSPACE_FURY:
            return HoneClaws()
        elif move == Moves.MEMENTO:
            return HyperspaceFury()
        elif move == Moves.NASTY_PLOT:
            return Memento()
        elif move == Moves.OBSTRUCT:
            return NastyPlot()
        elif move == Moves.PARTING_SHOT:
            return Obstruct()
        elif move == Moves.SNARL:
            return PartingShot()
        elif move == Moves.BREAKING_SWIPE:
            return Snarl()
        elif move == Moves.CLANGING_SCALES:
            return BreakingSwipe()
        elif move == Moves.CLANGOROUS_SOUL:
            return ClangingScales()
        elif move == Moves.DRACO_METEOR:
            return ClangorousSoul()
        elif move == Moves.DRAGON_DANCE:
            return DracoMeteor()
        elif move == Moves.SCALE_SHOT:
            return DragonDance()
        elif move == Moves.CHARGE:
            return ScaleShot()
        elif move == Moves.EERIE_IMPULSE:
            return Charge()
        elif move == Moves.ELECTROWEB:
            return EerieImpulse()
        elif move == Moves.MAGNETIC_FLUX:
            return Electroweb()
        elif move == Moves.AROMATIC_MIST:
            return MagneticFlux()
        elif move == Moves.BABY_DOLL_EYES:
            return AromaticMist()
        elif move == Moves.CHARM:
            return BabyDollEyes()
        elif move == Moves.DECORATE:
            return Charm()
        elif move == Moves.FLEUR_CANNON:
            return Decorate()
        elif move == Moves.FLOWER_SHIELD:
            return FleurCannon()
        elif move == Moves.GEOMANCY:
            return FlowerShield()
        elif move == Moves.SPIRIT_BREAK:
            return Geomancy()
        elif move == Moves.SPRINGTIDE_STORM:
            return SpiritBreak()
        elif move == Moves.BULK_UP:
            return SpringtideStorm()
        elif move == Moves.CLOSE_COMBAT:
            return BulkUp()
        elif move == Moves.HAMMER_ARM:
            return CloseCombat()
        elif move == Moves.LOW_SWEEP:
            return HammerArm()
        elif move == Moves.NO_RETREAT:
            return LowSweep()
        elif move == Moves.OCTOLOCK:
            return NoRetreat()
        elif move == Moves.POWER_UP_PUNCH:
            return Octolock()
        elif move == Moves.SUPERPOWER:
            return PowerUpPunch()
        elif move == Moves.ARMOR_CANNON:
            return Superpower()
        elif move == Moves.FIRE_LASH:
            return ArmorCannon()
        elif move == Moves.FLAME_CHARGE:
            return FireLash()
        elif move == Moves.MYSTICAL_FIRE:
            return FlameCharge()
        elif move == Moves.OVERHEAT:
            return MysticalFire()
        elif move == Moves.V_CREATE:
            return Overheat()
        elif move == Moves.DEFOG:
            return Vcreate()
        elif move == Moves.DRAGON_ASCENT:
            return Defog()
        elif move == Moves.FEATHER_DANCE:
            return DragonAscent()
        elif move == Moves.APPLE_ACID:
            return FeatherDance()
        elif move == Moves.COTTON_GUARD:
            return AppleAcid()
        elif move == Moves.COTTON_SPORE:
            return CottonGuard()
        elif move == Moves.DRUM_BEATING:
            return CottonSpore()
        elif move == Moves.GRAV_APPLE:
            return DrumBeating()
        elif move == Moves.LEAF_STORM:
            return GravApple()
        elif move == Moves.SPICY_EXTRACT:
            return LeafStorm()
        elif move == Moves.STRENGTH_SAP:
            return SpicyExtract()
        elif move == Moves.BULLDOZE:
            return StrengthSap()
        elif move == Moves.HEADLONG_RUSH:
            return Bulldoze()
        elif move == Moves.MUD_SHOT:
            return HeadlongRush()
        elif move == Moves.MUD_SLAP:
            return MudShot()
        elif move == Moves.ROTOTILLER:
            return MudSlap()
        elif move == Moves.SAND_ATTACK:
            return Rototiller()
        elif move == Moves.GLACIATE:
            return SandAttack()
        elif move == Moves.ICE_HAMMER:
            return Glaciate()
        elif move == Moves.ICY_WIND:
            return IceHammer()
        elif move == Moves.MOUNTAIN_GALE:
            return IcyWind()
        elif move == Moves.SNOWSCAPE:
            return MountainGale()
        elif move == Moves.ACUPRESSURE:
            return Snowscape()
        elif move == Moves.BELLY_DRUM:
            return Acupressure()
        elif move == Moves.CAPTIVATE:
            return BellyDrum()
        elif move == Moves.CONFIDE:
            return Captivate()
        elif move == Moves.DEFENSE_CURL:
            return Confide()
        elif move == Moves.DOUBLE_TEAM:
            return DefenseCurl()
        elif move == Moves.EXTREME_EVOBOOST:
            return DoubleTeam()
        elif move == Moves.FILLET_AWAY:
            return ExtremeEvoboost()
        elif move == Moves.FLASH:
            return FilletAway()
        elif move == Moves.GROWL:
            return Flash()
        elif move == Moves.GROWTH:
            return Growl()
        elif move == Moves.HARDEN:
            return Growth()
        elif move == Moves.HOWL:
            return Harden()
        elif move == Moves.LEER:
            return Howl()
        elif move == Moves.MINIMIZE:
            return Leer()
        elif move == Moves.NOBLE_ROAR:
            return Minimize()
        elif move == Moves.PLAY_NICE:
            return NobleRoar()
        elif move == Moves.RAGE:
            return PlayNice()
        elif move == Moves.RAPID_SPIN:
            return Rage()
        elif move == Moves.SCARY_FACE:
            return RapidSpin()
        elif move == Moves.SCREECH:
            return ScaryFace()
        elif move == Moves.SHARPEN:
            return Screech()
        elif move == Moves.SHELL_SMASH:
            return Sharpen()
        elif move == Moves.SKULL_BASH:
            return ShellSmash()
        elif move == Moves.SMOKESCREEN:
            return SkullBash()
        elif move == Moves.STUFF_CHEEKS:
            return Smokescreen()
        elif move == Moves.SWAGGER:
            return StuffCheeks()
        elif move == Moves.SWEET_SCENT:
            return Swagger()
        elif move == Moves.SWORDS_DANCE:
            return SweetScent()
        elif move == Moves.ACID_ARMOR:
            return SwordsDance()
        elif move == Moves.ACID_SPRAY:
            return AcidArmor()
        elif move == Moves.COIL:
            return AcidSpray()
        elif move == Moves.AGILITY:
            return Coil()
        elif move == Moves.AMNESIA:
            return Agility()
        elif move == Moves.BARRIER:
            return Amnesia()
        elif move == Moves.CALM_MIND:
            return Barrier()
        elif move == Moves.COSMIC_POWER:
            return CalmMind()
        elif move == Moves.ESPER_WING:
            return CosmicPower()
        elif move == Moves.KINESIS:
            return EsperWing()
        elif move == Moves.LUMINA_CRASH:
            return Kinesis()
        elif move == Moves.MEDITATE:
            return LuminaCrash()
        elif move == Moves.MYSTICAL_POWER:
            return Meditate()
        elif move == Moves.PSYCHO_BOOST:
            return MysticalPower()
        elif move == Moves.PSYSHIELD_BASH:
            return PsychoBoost()
        elif move == Moves.ROCK_POLISH:
            return PsyshieldBash()
        elif move == Moves.ROCK_TOMB:
            return RockPolish()
        elif move == Moves.AUTOTOMIZE:
            return RockTomb()
        elif move == Moves.IRON_DEFENSE:
            return Autotomize()
        elif move == Moves.KING_SHIELD:
            return IronDefense()
        elif move == Moves.MAKE_IT_RAIN:
            return KingShield()
        elif move == Moves.METAL_SOUND:
            return MakeItRain()
        elif move == Moves.SHELTER:
            return MetalSound()
        elif move == Moves.SHIFT_GEAR:
            return Shelter()
        elif move == Moves.SPIN_OUT:
            return ShiftGear()
        elif move == Moves.AQUA_STEP:
            return SpinOut()
        elif move == Moves.CHILLING_WATER:
            return AquaStep()
        elif move == Moves.ANCHOR_SHOT:
            return ChillingWater()
        elif move == Moves.BEHEMOTH_BASH:
            return AnchorShot()
        elif move == Moves.BEHEMOTH_BLADE:
            return BehemothBash()
        elif move == Moves.BULLET_PUNCH:
            return BehemothBlade()
        elif move == Moves.CORKSCREW_CRASH:
            return BulletPunch()
        elif move == Moves.DOOM_DESIRE:
            return CorkscrewCrash()
        elif move == Moves.FLASH_CANNON:
            return DoomDesire()
        elif move == Moves.GEAR_GRIND:
            return FlashCannon()
        elif move == Moves.GEAR_UP:
            return GearGrind()
        elif move == Moves.GIGATON_HAMMER:
            return GearUp()
        elif move == Moves.GYRO_BALL:
            return GigatonHammer()
        elif move == Moves.HEAVY_SLAM:
            return GyroBall()
        elif move == Moves.IRON_TAIL:
            return HeavySlam()
        elif move == Moves.MAGNET_BOMB:
            return IronTail()
        elif move == Moves.METAL_BURST:
            return MagnetBomb()
        elif move == Moves.METAL_CLAW:
            return MetalBurst()
        elif move == Moves.METEOR_MASH:
            return MetalClaw()
        elif move == Moves.MIRROR_SHOT:
            return MeteorMash()
        elif move == Moves.SEARING_SUNRAZE_SMASH:
            return MirrorShot()
        elif move == Moves.SMART_STRIKE:
            return SearingSunrazeSmash()
        elif move == Moves.STEEL_BEAM:
            return SmartStrike()
        elif move == Moves.STEEL_ROLLER:
            return SteelBeam()
        elif move == Moves.STEEL_WING:
            return SteelRoller()
        elif move == Moves.SUNSTEEL_STRIKE:
            return SteelWing()
        elif move == Moves.AQUA_CUTTER:
            return SunsteelStrike()
        elif move == Moves.AQUA_JET:
            return AquaCutter()
        elif move == Moves.AQUA_RING:
            return AquaJet()
        elif move == Moves.AQUA_TAIL:
            return AquaRing()
        elif move == Moves.BOUNCY_BUBBLE:
            return AquaTail()
        elif move == Moves.BRINE:
            return BouncyBubble()
        elif move == Moves.BUBBLE:
            return Brine()
        elif move == Moves.BUBBLE_BEAM:
            return Bubble()
        elif move == Moves.CLAMP:
            return BubbleBeam()
        elif move == Moves.CRABHAMMER:
            return Clamp()
        elif move == Moves.DIVE:
            return Crabhammer()
        elif move == Moves.FISHIOUS_REND:
            return Dive()
        elif move == Moves.FLIP_TURN:
            return FishiousRend()
        elif move == Moves.HYDRO_CANNON:
            return FlipTurn()
        elif move == Moves.HYDRO_PUMP:
            return HydroCannon()
        elif move == Moves.HYDRO_STEAM:
            return HydroPump()
        elif move == Moves.HYDRO_VORTEX:
            return HydroSteam()
        elif move == Moves.JET_PUNCH:
            return HydroVortex()
        elif move == Moves.LIFE_DEW:
            return JetPunch()
        elif move == Moves.LIQUIDATION:
            return LifeDew()
        elif move == Moves.MUDDY_WATER:
            return Liquidation()
        elif move == Moves.OCEANIC_OPERETTA:
            return MuddyWater()
        elif move == Moves.OCTAZOOKA:
            return OceanicOperetta()
        elif move == Moves.ORIGIN_PULSE:
            return Octazooka()
        elif move == Moves.RAIN_DANCE:
            return OriginPulse()
        elif move == Moves.RAZOR_SHELL:
            return RainDance()
        elif move == Moves.SNIPE_SHOT:
            return RazorShell()
        elif move == Moves.SOAK:
            return SnipeShot()
        elif move == Moves.SPARKLING_ARIA:
            return Soak()
        elif move == Moves.SURF:
            return SparklingAria()
        elif move == Moves.SURGING_STRIKES:
            return Surf()
        elif move == Moves.TRIPLE_DIVE:
            return SurgingStrikes()
        elif move == Moves.WATER_GUN:
            return TripleDive()
        elif move == Moves.WATER_PLEDGE:
            return WaterGun()
        elif move == Moves.WATER_PULSE:
            return WaterPledge()
        elif move == Moves.WATER_SHURIKEN:
            return WaterPulse()
        elif move == Moves.WATER_SPORT:
            return WaterShuriken()
        elif move == Moves.WATER_SPOUT:
            return WaterSport()
        elif move == Moves.WAVE_CRASH:
            return WaterSpout()
        elif move == Moves.WHIRLPOOL:
            return WaveCrash()
        elif move == Moves.WITHDRAW:
            return Whirlpool()
