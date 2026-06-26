---
layout: post
title: "Algorithm Templates: Math & Geometry"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates math geometry
permalink: /posts/2025-10-29-leetcode-templates-math-geometry/
tags: [leetcode, templates, math, geometry]
---

Minimal, copy-paste C++ for combinatorics (nCk mod P) and 2D geometry primitives (cross product, point on segment).

<svg viewBox="0 0 680 200" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="340" y="18" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">Cross Product — determines turn direction</text>
  <line x1="80" y1="150" x2="600" y2="150" stroke="#E0DDD8" stroke-width="1"/>
  <line x1="80" y1="150" x2="80" y2="40" stroke="#E0DDD8" stroke-width="1"/>
  <circle cx="120" cy="130" r="6" fill="#D4D8E0" stroke="#B8B5B0"/><text x="120" y="148" font-size="10" fill="#5A5752" text-anchor="middle">A</text>
  <circle cx="280" cy="90" r="6" fill="#D4D8D0" stroke="#B8B5B0"/><text x="280" y="82" font-size="10" fill="#5A5752" text-anchor="middle">B</text>
  <circle cx="420" cy="60" r="6" fill="#E8D5D0" stroke="#B8B5B0"/><text x="420" y="52" font-size="10" fill="#5A5752" text-anchor="middle">C</text>
  <line x1="120" y1="130" x2="280" y2="90" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="280" y1="90" x2="420" y2="60" stroke="#B8B5B0" stroke-width="2"/>
  <text x="340" y="130" font-size="11" fill="#5A5752" text-anchor="middle">cross(A,B,C) = (B-A) × (C-A)</text>
  <text x="340" y="152" font-size="10" fill="#3A6B3A" text-anchor="middle">&gt; 0 → counter-clockwise (left turn) | &lt; 0 → clockwise | = 0 → collinear</text>
  <text x="340" y="175" font-size="10" fill="#5A5752" text-anchor="middle">Used for: convex hull, polygon area, point-in-polygon, segment intersection</text>
</svg>

## Contents

- [Combinatorics (nCk mod P)](#combinatorics-nck-mod-p)
- [Geometry Primitives (2D)](#geometry-primitives-2d)

## Combinatorics (nCk mod P)

```cpp
const int MOD=1'000'000'007; const int N=200000;
long long modexp(long long a,long long e){ long long r=1%MOD; while(e){ if(e&1) r=r*a%MOD; a=a*a%MOD; e>>=1; } return r; }
vector<long long> fact(N+1), invfact(N+1);
void initComb(){ fact[0]=1; for(int i=1;i<=N;++i) fact[i]=fact[i-1]*i%MOD; invfact[N]=modexp(fact[N], MOD-2); for(int i=N;i>0;--i) invfact[i-1]=invfact[i]*i%MOD; }
long long nCk(int n,int k){ if(k<0||k>n) return 0; return fact[n]*invfact[k]%MOD*invfact[n-k]%MOD; }
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 62 | Unique Paths | [Link](https://leetcode.com/problems/unique-paths/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/24/medium-62-unique-paths/) |
| 172 | Factorial Trailing Zeroes | [Link](https://leetcode.com/problems/factorial-trailing-zeroes/) | - |

## Geometry Primitives (2D)

```cpp
struct P{ long long x,y; };
long long cross(const P& a,const P& b,const P& c){ return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x); }
bool onSeg(const P&a,const P&b,const P&c){ return min(a.x,b.x)<=c.x&&c.x<=max(a.x,b.x)&&min(a.y,b.y)<=c.y&&c.y<=max(a.y,b.y) && cross(a,b,c)==0; }
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 149 | Max Points on a Line | [Link](https://leetcode.com/problems/max-points-on-a-line/) | - |
| 223 | Rectangle Area | [Link](https://leetcode.com/problems/rectangle-area/) | - |
| 1344 | Angle Between Hands of a Clock | [Link](https://leetcode.com/problems/angle-between-hands-of-a-clock/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/04/medium-1344-angle-between-hands-of-a-clock/) |

## More templates

- **DP (counting, paths):** [Dynamic Programming](/posts/2025-10-29-leetcode-templates-dp/)
- **Data structures, Graph, Search:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
