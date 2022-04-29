import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from tqdm import tqdm
import argparse

from entities import Ball
from geometry import Vector


def main(N, rain_pathlen, velocity, random_seed):
    np.random.seed(random_seed)

    body = Ball(Vector(np.zeros(2)), 1.0)
    drops = [
        Vector(coords)
        for coords in np.c_[
            np.random.uniform(-60.0, 60.0, size=N),
            np.random.uniform(-1.0, 60.0, size=N),
        ]
    ]
    displacement = Vector(np.array([velocity * rain_pathlen, -rain_pathlen]))

    alphas = np.linspace(0.0, 2 * np.pi, 20)
    plt.gca().add_patch(
        mpl.patches.Polygon(
            body.R * np.c_[np.sin(alphas), np.cos(alphas)] + body.location.data,
            facecolor="#505050",
            edgecolor="#000000",
            zorder=-1000,
        )
    )
    collisions = [body.line_collide(drop, drop + displacement) for drop in tqdm(drops)]
    plt.scatter(
        *zip(*[d.data for d in drops]), c=collisions, s=0.2, cmap="bwr"
    )

    nhits = sum(collisions)
    result_str = f"# hits = {nhits} +/- {nhits**0.5:.0f}"
    print(result_str)
    plt.text(-50, 60, result_str, bbox=dict(facecolor="white"))
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-N", type=int, default=500000)
    parser.add_argument("--rain_pathlen", type=float, default=50.0)
    parser.add_argument("--velocity", type=float, default=0.0)
    parser.add_argument("--random_seed", type=int, default=42)

    args = parser.parse_args()
    main(
        N=args.N,
        rain_pathlen=args.rain_pathlen,
        velocity=args.velocity,
        random_seed=args.random_seed,
    )
