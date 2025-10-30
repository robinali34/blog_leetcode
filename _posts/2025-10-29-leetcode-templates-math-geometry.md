---
layout: post
title: "LeetCode Templates: Math & Geometry"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates math geometry
permalink: /posts/2025-10-29-leetcode-templates-math-geometry/
tags: [leetcode, templates, math, geometry]
---

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

| ID | Title | Link |
|---|---|---|
| 62 | Unique Paths | [Unique Paths](https://leetcode.com/problems/unique-paths/) |
| 172 | Factorial Trailing Zeroes | [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/) |

## Geometry Primitives (2D)

```cpp
struct P{ long long x,y; };
long long cross(const P& a,const P& b,const P& c){ return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x); }
bool onSeg(const P&a,const P&b,const P&c){ return min(a.x,b.x)<=c.x&&c.x<=max(a.x,b.x)&&min(a.y,b.y)<=c.y&&c.y<=max(a.y,b.y) && cross(a,b,c)==0; }
```

| ID | Title | Link |
|---|---|---|
| 149 | Max Points on a Line | [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) |
| 223 | Rectangle Area | [Rectangle Area](https://leetcode.com/problems/rectangle-area/) |
