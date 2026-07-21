export interface CulturalLabel {
  readonly languageTag: string;
  readonly value: string;
}

export interface PatternLineSegment {
  readonly fromCatalogueId: string;
  readonly toCatalogueId: string;
}

export interface SkyPattern {
  readonly stableId: string;
  readonly contentVersion: string;
  readonly names: readonly CulturalLabel[];
  readonly memberStarCatalogueIds: readonly string[];
  readonly lineSegments: readonly PatternLineSegment[];
  readonly culturalReviewStatus: string;
}

export type GuidanceSource =
  | { readonly kind: 'pattern'; readonly stableId: string }
  | { readonly kind: 'star'; readonly catalogueId: string };

export type GuidanceTarget =
  GuidanceSource | { readonly kind: 'direction'; readonly stableId: string };

export interface InstructionalLineOrVector {
  readonly kind: string;
  readonly payload: unknown;
}

export interface GuidanceRelationship {
  readonly stableId: string;
  readonly relationshipVersion: string;
  readonly source: GuidanceSource;
  readonly target: GuidanceTarget;
  readonly relationshipType: string;
  readonly instructionalLineOrVector: InstructionalLineOrVector;
  readonly explanation: string;
  readonly applicableScenarioIds: readonly string[];
  readonly verificationStatus: string;
}

export interface LessonRouteStep {
  readonly guidanceRelationshipId: string;
  readonly learningStepId: string;
}

export interface LessonRoute {
  readonly stableId: string;
  readonly routeVersion: string;
  readonly routeStatus: string;
  readonly orderedLearningSteps: readonly LessonRouteStep[];
  readonly prerequisiteSkillIds: readonly string[];
  readonly allowedAlternativeGuidancePathIds: readonly string[];
  readonly scaffoldConfigurationId: string;
}
