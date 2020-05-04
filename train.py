import argparse
import shlex
import sys
import time
import os
import platform

from envs import chess

from envs.chess import chess_name2temp_goals, chess_name2robot_feature_ext
from utils import name2algorithm, check_in_float_range, CHESS, Config, SARSA

parser = argparse.ArgumentParser(description='Execute a Reinforcement Learning process')
parser.add_argument('--algorithm',      default=SARSA, choices=list(name2algorithm.keys()),                help="TD algorithm variant. The possible values are: '" + "', '".join(list(name2algorithm.keys())) + "'")
parser.add_argument('--episodes',       default=10000, type=int,                                           help='Number of episodes.')
parser.add_argument('--gamma',          default=1.0,   type=check_in_float_range(0.0, 1.0, False,  False),  help="The discount factor. Must fall into [0, 1].")
parser.add_argument('--alpha',          default=0.1,   type=check_in_float_range(0.0, 1.0, False, True),   help="The learning rate. Must fall into (0, 1], or None (adaptive). Default: 0.1")
parser.add_argument('--epsilon',        default=0.1,   type=check_in_float_range(0.0, 1.0, False,  False), help="The epsilon in eps-greedy. Must fall into [0, 1].")
parser.add_argument('--lambda',         default=0.0,   type=check_in_float_range(0.0, 1.0, False,  False), help="Lambda in TD(Lambda). Default: 0 (classical TD)", dest="lambda_")
parser.add_argument('--reward_shaping', action='store_true',        help="Enable reward shaping")
parser.add_argument('--on_the_fly',     action='store_true',        help="Enable on-the-fly construction")
parser.add_argument('--render',         default=True,   action='store_true',        help='Enable rendering.')
parser.add_argument('--datadir',        default="data",             help='Directory to store the output of the process.')
parser.add_argument('--verbosity',      default=1,      type=int, choices=[0,1,2],  help='Verbosity {0,1,2}')

# Environment subparser
env_subparser = parser.add_subparsers(title="Environment selection", metavar="ENVIRONMENT", description="choose the environment", dest='cmd')
env_subparser.required = True

# Chess
chess_subparser = env_subparser.add_parser(CHESS, help="use the Chess environment")
chess_subparser.add_argument("--robot_feature_space", default="N", choices=sorted(chess_name2robot_feature_ext.keys()), help="Specify the feature space for the robot. N=normal, D=differential")
chess_subparser.add_argument("--temp_goal", choices=sorted(chess_name2temp_goals.keys()), help="Temporal goal. Ordered visit of colors.")



name2module = {

    CHESS: chess
}


def print_info(config, args):
    with open("experiment.info", "w") as f:
        f.write(str(config))
        f.write("\n")
        f.write(str(args))


def main(cli_input):
    if type(cli_input)==str:
        arguments = shlex.split(cli_input)
    elif type(cli_input) == list:
        arguments = cli_input
    else:
        raise Exception

    args = parser.parse_args(arguments)

    eval_and_view = False
    config = Config(episodes=args.episodes,
                    algorithm=args.algorithm,
                    gamma=args.gamma,
                    alpha=args.alpha,
                    eval=eval_and_view,
                    epsilon=args.epsilon,
                    lambda_=args.lambda_,
                    reward_shaping=args.reward_shaping,
                    on_the_fly=args.on_the_fly,
                    datadir=args.datadir,
                    render=eval_and_view,
                    verbosity=args.verbosity)

    print(config)
    # dispatching
    cmd = args.cmd
    name2module[cmd].run_experiment(config, args)


if __name__ == '__main__':
    main(sys.argv[1:])

    print(platform.system())

    if "Darwin" in platform.system():
        os.system('say "your program has finished"')
    elif "Linux" in platform.system():
        os.system('spd-say "your program has finished"')

    elif "Windows" in platform.system():
        import winsound
        duration = 1000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)
